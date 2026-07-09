"""評価結果を Markdown レポートとして出力する。"""

from __future__ import annotations

import os
from datetime import date

from .metrics import CouncilStats, MemberStats

_CRITERIA_LABELS = {
    "specificity": "具体性",
    "proposal": "政策提案性",
    "follow_up": "追及・検証力",
    "citizen_relevance": "市民関連性",
    "clarity": "論点明確さ",
}

_DISCLAIMER = """\
> **注意**: 本レポートは公開されている会議録等をもとに機械的・AI的に生成した参考資料であり、
> 議員個人の人格や能力を断定するものではありません。会議録に現れる本会議での発言は
> 議員活動の一部にすぎず、委員会活動・地域活動などは反映されていません。
> 評価基準と限界は docs/evaluation_criteria.md を参照してください。
"""


def _score_bar(score: int) -> str:
    return "★" * score + "☆" * (5 - score)


def write_reports(
    members: dict[str, MemberStats],
    council: CouncilStats,
    out_dir: str,
    member_evals: dict[str, dict] | None = None,
    council_eval: dict | None = None,
) -> list[str]:
    """レポート一式を out_dir に書き出し、生成したファイルパスを返す。"""
    member_evals = member_evals or {}
    os.makedirs(os.path.join(out_dir, "members"), exist_ok=True)
    written: list[str] = []

    council_path = os.path.join(out_dir, "council_report.md")
    with open(council_path, "w", encoding="utf-8") as f:
        f.write(_render_council(members, council, member_evals, council_eval))
    written.append(council_path)

    for name, stats in members.items():
        path = os.path.join(out_dir, "members", f"{name}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(_render_member(stats, member_evals.get(name)))
        written.append(path)

    return written


def _render_council(
    members: dict[str, MemberStats],
    council: CouncilStats,
    member_evals: dict[str, dict],
    council_eval: dict | None,
) -> str:
    lines: list[str] = []
    lines.append("# 議会評価レポート")
    lines.append("")
    lines.append(f"生成日: {date.today().isoformat()}")
    lines.append("")
    lines.append(_DISCLAIMER)

    lines.append("## 議会全体の定量指標")
    lines.append("")
    lines.append("| 指標 | 値 |")
    lines.append("| --- | --- |")
    lines.append(f"| 解析した会議録数 | {council.total_sessions} |")
    lines.append(f"| うち一般質問を含む会議 | {council.gq_sessions} |")
    lines.append(f"| 総発言数 | {council.total_utterances} |")
    lines.append(
        f"| 議員発言 / 執行部発言 | {council.member_utterances} / {council.executive_utterances} |"
    )
    lines.append(
        f"| 議員発言文字数 / 執行部発言文字数 | {council.member_chars:,} / {council.executive_chars:,} |"
    )
    lines.append(
        f"| 発言議員数 / 名簿議員数 | {council.speaking_members} / {council.roster_size} "
        f"(参加率 {council.participation_rate:.0%}) |"
    )
    lines.append(
        f"| 発言量の偏り(ジニ係数) | {council.speech_gini:.2f} (0=均等, 1=一部に集中) |"
    )
    if council.bills:
        lines.append(f"| 賛否データのある議案数 | {len(council.bills)} |")
        lines.append(f"| 全会一致率 | {council.unanimous_rate:.0%} |")
    lines.append("")

    lines.append("## 議員別 定量ランキング(発言文字数順)")
    lines.append("")
    lines.append("| 順位 | 議員名 | 会派 | 発言回数 | 発言文字数 | 一般質問回数 |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    ranked = sorted(members.values(), key=lambda m: m.total_chars, reverse=True)
    for i, m in enumerate(ranked, start=1):
        lines.append(
            f"| {i} | [{m.name}](members/{m.name}.md) | {m.kaiha or '-'} "
            f"| {m.utterance_count} | {m.total_chars:,} | {m.gq_count} |"
        )
    lines.append("")

    if member_evals:
        lines.append("## 議員別 定性評価サマリー(AI・5点満点)")
        lines.append("")
        header = " | ".join(_CRITERIA_LABELS.values())
        lines.append(f"| 議員名 | {header} | 合計 |")
        lines.append("| --- |" + " --- |" * (len(_CRITERIA_LABELS) + 1))
        eval_rows = []
        for name, ev in member_evals.items():
            scores = ev.get("scores", {})
            total = sum(scores.get(k, 0) for k in _CRITERIA_LABELS)
            eval_rows.append((total, name, scores))
        for total, name, scores in sorted(eval_rows, reverse=True):
            cells = " | ".join(str(scores.get(k, "-")) for k in _CRITERIA_LABELS)
            lines.append(f"| [{name}](members/{name}.md) | {cells} | **{total}** |")
        lines.append("")

    if council.bills:
        lines.append("## 議案別の賛否")
        lines.append("")
        lines.append("| 議案番号 | 議案名 | 賛否内訳 |")
        lines.append("| --- | --- | --- |")
        for no, bill in council.bills.items():
            breakdown = ", ".join(f"{k} {v}" for k, v in bill["votes"].items())
            lines.append(f"| {no} | {bill['name']} | {breakdown} |")
        lines.append("")

    if council_eval:
        lines.append("## 議会全体の定性評価(AI)")
        lines.append("")
        lines.append(f"**総評**: {council_eval.get('summary', '')}")
        lines.append("")
        lines.append(f"- **審議の実質性**: {council_eval.get('deliberation_quality', '')}")
        lines.append(f"- **答弁の質**: {council_eval.get('answer_quality', '')}")
        for label, key in (
            ("注目すべき議論", "notable_debates"),
            ("懸念点", "concerns"),
            ("改善提案", "recommendations"),
        ):
            items = council_eval.get(key) or []
            if items:
                lines.append(f"- **{label}**:")
                for item in items:
                    lines.append(f"  - {item}")
        lines.append("")

    return "\n".join(lines) + "\n"


def _render_member(stats: MemberStats, ev: dict | None) -> str:
    lines: list[str] = []
    lines.append(f"# 議員評価: {stats.name}")
    lines.append("")
    lines.append(_DISCLAIMER)
    lines.append("## 定量指標")
    lines.append("")
    lines.append("| 指標 | 値 |")
    lines.append("| --- | --- |")
    if stats.kaiha:
        lines.append(f"| 会派 | {stats.kaiha} |")
    if stats.seat:
        lines.append(f"| 議席番号 | {stats.seat} |")
    lines.append(f"| 発言回数 | {stats.utterance_count} |")
    lines.append(f"| 発言文字数 | {stats.total_chars:,} |")
    lines.append(f"| 発言した会議数 | {stats.session_count} |")
    lines.append(f"| 一般質問を行った会議数 | {stats.gq_count} |")
    lines.append(f"| 平均発言長(文字) | {stats.avg_chars:,.0f} |")
    lines.append("")

    if stats.votes:
        lines.append("## 議案への賛否")
        lines.append("")
        lines.append("| 議案番号 | 賛否 |")
        lines.append("| --- | --- |")
        for no, decision in stats.votes.items():
            lines.append(f"| {no} | {decision} |")
        lines.append("")

    if ev:
        scores = ev.get("scores", {})
        lines.append("## 定性評価(AI・5点満点)")
        lines.append("")
        lines.append(f"信頼度: {ev.get('confidence', '-')}")
        lines.append("")
        lines.append("| 基準 | スコア | |")
        lines.append("| --- | --- | --- |")
        for key, label in _CRITERIA_LABELS.items():
            s = scores.get(key)
            bar = _score_bar(s) if isinstance(s, int) else ""
            lines.append(f"| {label} | {s if s is not None else '-'} | {bar} |")
        lines.append("")
        if ev.get("themes"):
            lines.append("**取り上げたテーマ**: " + "、".join(ev["themes"]))
            lines.append("")
        lines.append(f"**総評**: {ev.get('summary', '')}")
        lines.append("")
        lines.append(f"**強み**: {ev.get('strengths', '')}")
        lines.append("")
        lines.append(f"**改善が期待される点**: {ev.get('improvements', '')}")
        lines.append("")
        if ev.get("evidence"):
            lines.append("### 評価根拠(会議録からの引用)")
            lines.append("")
            for e in ev["evidence"]:
                lines.append(f"- **{e.get('criterion', '')}**: 「{e.get('quote', '')}」")
                lines.append(f"  - {e.get('comment', '')}")
            lines.append("")
    elif stats.utterance_count == 0:
        lines.append("## 定性評価")
        lines.append("")
        lines.append("解析対象の会議録に本会議での発言が見つからなかったため、評価はありません。")
        lines.append("")

    return "\n".join(lines) + "\n"
