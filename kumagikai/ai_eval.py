"""Claude API による定性評価。

docs/evaluation_criteria.md のルーブリックに沿って、
議員個人の一般質問・発言と、議会全体の審議を評価する。

利用には `pip install anthropic` と ANTHROPIC_API_KEY が必要。
どちらも無い環境では run_evaluation.py が自動的にこのステップをスキップする。
"""

from __future__ import annotations

import json

DEFAULT_MODEL = "claude-opus-4-8"

# 1議員あたりAPIに渡す発言テキストの上限(文字)
MEMBER_TEXT_LIMIT = 30_000
COUNCIL_TEXT_LIMIT = 60_000

_SYSTEM_PROMPT = """\
あなたは地方議会のウォッチングを行う中立的なアナリストです。
与えられた会議録の発言内容【のみ】を根拠に、透明なルーブリックに沿って評価します。

厳守事項:
- 会議録に書かれていないことを推測して評価しない。
- 人格・思想信条ではなく、議会活動(質問・提案・追及)の質だけを評価する。
- 全員に同一の基準を適用する。所属会派・政党による有利不利をつけない。
- 各スコアには必ず会議録からの短い引用(根拠)を添える。
- 断定的な人物評価や名誉を毀損しうる表現は使わない。改善提案は建設的に書く。
- 発言量が少なく判断材料が不足する場合は、無理に採点せず confidence を下げ、その旨を明記する。
"""

_MEMBER_SCHEMA = {
    "type": "object",
    "properties": {
        "scores": {
            "type": "object",
            "properties": {
                "specificity": {"type": "integer"},      # 具体性(数字・現場・固有の事実)
                "proposal": {"type": "integer"},          # 政策提案性(対案・提案の有無と質)
                "follow_up": {"type": "integer"},         # 追及・検証力(再質問・答弁の掘り下げ)
                "citizen_relevance": {"type": "integer"}, # 市民生活との関連の明確さ
                "clarity": {"type": "integer"},           # 論点の明確さ・簡潔さ
            },
            "required": [
                "specificity",
                "proposal",
                "follow_up",
                "citizen_relevance",
                "clarity",
            ],
            "additionalProperties": False,
        },
        "evidence": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "criterion": {"type": "string"},
                    "quote": {"type": "string"},
                    "comment": {"type": "string"},
                },
                "required": ["criterion", "quote", "comment"],
                "additionalProperties": False,
            },
        },
        "themes": {"type": "array", "items": {"type": "string"}},
        "strengths": {"type": "string"},
        "improvements": {"type": "string"},
        "summary": {"type": "string"},
        "confidence": {"type": "string", "enum": ["high", "medium", "low"]},
    },
    "required": [
        "scores",
        "evidence",
        "themes",
        "strengths",
        "improvements",
        "summary",
        "confidence",
    ],
    "additionalProperties": False,
}

_COUNCIL_SCHEMA = {
    "type": "object",
    "properties": {
        "deliberation_quality": {"type": "string"},  # 審議の実質性の所見
        "answer_quality": {"type": "string"},        # 執行部答弁の具体性の所見
        "notable_debates": {"type": "array", "items": {"type": "string"}},
        "concerns": {"type": "array", "items": {"type": "string"}},
        "recommendations": {"type": "array", "items": {"type": "string"}},
        "summary": {"type": "string"},
    },
    "required": [
        "deliberation_quality",
        "answer_quality",
        "notable_debates",
        "concerns",
        "recommendations",
        "summary",
    ],
    "additionalProperties": False,
}


def _client():
    try:
        import anthropic
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError(
            "anthropic パッケージが見つかりません。`pip install anthropic` を実行してください。"
        ) from exc
    return anthropic.Anthropic()


def _create(client, model: str, schema: dict, prompt: str) -> dict:
    response = client.messages.create(
        model=model,
        max_tokens=16000,
        thinking={"type": "adaptive"},
        system=_SYSTEM_PROMPT,
        output_config={"format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": prompt}],
    )
    if response.stop_reason == "refusal":
        raise RuntimeError("モデルが評価を拒否しました(refusal)。入力を確認してください。")
    text = next(b.text for b in response.content if b.type == "text")
    return json.loads(text)


def evaluate_member(
    name: str, texts: list[str], model: str = DEFAULT_MODEL, client=None
) -> dict:
    """議員1名の発言集合をルーブリック評価する。"""
    client = client or _client()
    joined = "\n\n---\n\n".join(texts)
    if len(joined) > MEMBER_TEXT_LIMIT:
        joined = joined[:MEMBER_TEXT_LIMIT] + "\n…(以下省略)"
    prompt = f"""\
次の発言は、市議会の会議録から抽出した議員「{name}」の発言(一般質問・質疑・討論など)です。

各基準を1〜5で採点してください(3が「標準的な水準」):
- specificity: 具体性。数字・現場の事実・固有の事例に基づいているか
- proposal: 政策提案性。批判だけでなく実行可能な対案・提案を示しているか
- follow_up: 追及・検証力。答弁を踏まえた再質問や過去の答弁のフォローがあるか
- citizen_relevance: 市民生活との関連。誰のどんな課題かが明確か
- clarity: 論点の明確さ。質問の趣旨が簡潔で答弁側に伝わる形か

--- 発言ここから ---
{joined}
--- 発言ここまで ---
"""
    return _create(client, model, _MEMBER_SCHEMA, prompt)


def evaluate_council(
    minutes_texts: list[str], model: str = DEFAULT_MODEL, client=None
) -> dict:
    """議会全体(審議の実質性・答弁の質)を評価する。"""
    client = client or _client()
    joined = "\n\n===== 会議録の区切り =====\n\n".join(minutes_texts)
    if len(joined) > COUNCIL_TEXT_LIMIT:
        joined = joined[:COUNCIL_TEXT_LIMIT] + "\n…(以下省略)"
    prompt = f"""\
次は市議会本会議の会議録(抜粋)です。議会全体としての審議について所見をまとめてください。

観点:
- 審議の実質性: 質問と答弁がかみ合っているか。形式的なやり取りに終始していないか
- 答弁の質: 執行部の答弁が具体的か。「検討します」型の答弁で終わっていないか
- 注目すべき議論: 政策的に重要と思われるやり取り
- 懸念点と、議会運営・審議の改善につながる提案

--- 会議録ここから ---
{joined}
--- 会議録ここまで ---
"""
    return _create(client, model, _COUNCIL_SCHEMA, prompt)
