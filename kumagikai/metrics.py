"""発言データ・賛否データから定量指標を算出する。"""

from __future__ import annotations

import csv
import json
import unicodedata
from dataclasses import dataclass, field

from .parse import Minutes, normalize_name


@dataclass
class MemberStats:
    name: str
    kaiha: str = ""            # 会派
    seat: str = ""             # 議席番号など
    utterance_count: int = 0   # 発言回数
    total_chars: int = 0       # 発言文字数(空白除く)
    sessions: set = field(default_factory=set)          # 発言した会議(ファイル)
    gq_sessions: set = field(default_factory=set)       # 一般質問で発言した会議
    texts: list = field(default_factory=list)           # 発言本文(AI評価用)
    votes: dict = field(default_factory=dict)           # 議案番号 -> 賛否

    @property
    def session_count(self) -> int:
        return len(self.sessions)

    @property
    def gq_count(self) -> int:
        return len(self.gq_sessions)

    @property
    def avg_chars(self) -> float:
        return self.total_chars / self.utterance_count if self.utterance_count else 0.0


@dataclass
class CouncilStats:
    total_sessions: int = 0
    gq_sessions: int = 0
    total_utterances: int = 0
    member_utterances: int = 0
    executive_utterances: int = 0
    member_chars: int = 0
    executive_chars: int = 0
    speaking_members: int = 0       # 発言のあった議員数
    roster_size: int = 0            # 名簿上の議員数(名簿がある場合)
    participation_rate: float = 0.0  # 発言議員 / 名簿議員
    speech_gini: float = 0.0        # 議員間の発言量の偏り (0=均等, 1=独占)
    bills: dict = field(default_factory=dict)   # 議案番号 -> {"name":, "votes": {賛否: 人数}}
    unanimous_rate: float = 0.0     # 全会一致だった議案の割合


def load_members(path: str) -> dict[str, dict]:
    """議員名簿JSONを読み込み、正規化名 -> 属性 の辞書を返す。

    JSON形式: {"members": [{"name": "...", "kaiha": "...", "seat": ...}, ...]}
    """
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    roster: dict[str, dict] = {}
    for m in data.get("members", []):
        roster[normalize_name(m["name"])] = m
    return roster


def load_votes(path: str) -> list[dict]:
    """賛否CSVを読み込む。

    列: 議案番号,議案名,議員名,賛否 (賛否は 賛成/反対/退席/欠席 など)
    """
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _gini(values: list[int]) -> float:
    """発言量分布のジニ係数(議員間の活動の偏りの指標)。"""
    vals = sorted(v for v in values if v >= 0)
    n = len(vals)
    total = sum(vals)
    if n == 0 or total == 0:
        return 0.0
    cum = 0
    weighted = 0
    for i, v in enumerate(vals, start=1):
        cum += v
        weighted += cum
    # Gini = 1 - 2 * (加重累積 - 総和/2) の標準式を離散近似
    return (n + 1 - 2 * weighted / total) / n


def compute_stats(
    minutes_list: list[Minutes],
    roster: dict[str, dict] | None = None,
    votes: list[dict] | None = None,
) -> tuple[dict[str, MemberStats], CouncilStats]:
    """会議録(+名簿+賛否)から議員別・議会全体の統計を計算する。"""
    roster = roster or {}
    members: dict[str, MemberStats] = {}
    council = CouncilStats(total_sessions=len(minutes_list))

    def member_entry(name: str) -> MemberStats:
        if name not in members:
            info = roster.get(name, {})
            members[name] = MemberStats(
                name=name,
                kaiha=str(info.get("kaiha", "")),
                seat=str(info.get("seat", "")),
            )
        return members[name]

    for minutes in minutes_list:
        is_gq = minutes.is_general_question
        if is_gq:
            council.gq_sessions += 1
        for u in minutes.utterances:
            council.total_utterances += 1
            # 名簿に載っている名前は肩書きが取れなくても議員として扱う
            role = u.role
            if role == "unknown" and normalize_name(u.speaker) in roster:
                role = "member"
            if role == "member":
                council.member_utterances += 1
                council.member_chars += u.chars
                stats = member_entry(u.speaker)
                stats.utterance_count += 1
                stats.total_chars += u.chars
                stats.sessions.add(minutes.source)
                if is_gq:
                    stats.gq_sessions.add(minutes.source)
                stats.texts.append(u.text)
            elif role == "executive":
                council.executive_utterances += 1
                council.executive_chars += u.chars

    # 名簿にあって一度も発言していない議員も統計対象に含める
    for name in roster:
        member_entry(name)

    council.speaking_members = sum(1 for m in members.values() if m.utterance_count)
    council.roster_size = len(roster) if roster else len(members)
    if council.roster_size:
        council.participation_rate = council.speaking_members / council.roster_size
    council.speech_gini = _gini([m.total_chars for m in members.values()])

    if votes:
        for row in votes:
            bill_no = row.get("議案番号", "").strip()
            if not bill_no:
                continue
            bill = council.bills.setdefault(
                bill_no, {"name": row.get("議案名", "").strip(), "votes": {}}
            )
            decision = unicodedata.normalize("NFKC", row.get("賛否", "").strip())
            bill["votes"][decision] = bill["votes"].get(decision, 0) + 1
            name = normalize_name(row.get("議員名", ""))
            if name:
                member_entry(name).votes[bill_no] = decision
        if council.bills:
            unanimous = sum(
                1
                for b in council.bills.values()
                if len({d for d in b["votes"] if d in ("賛成", "反対")}) <= 1
            )
            council.unanimous_rate = unanimous / len(council.bills)

    return members, council
