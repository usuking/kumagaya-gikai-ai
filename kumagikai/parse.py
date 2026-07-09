"""会議録テキストを発言者ごとの発言に分解するパーサ。

想定する入力は、会議録検索システム(kaigiroku.net 等)からテキスト保存した
本会議録で、次のような形式の発言行を含むもの:

    ◯議長(山川太郎君) これより本日の会議を開きます。
    ◯１２番(青木一郎君) 通告に従いまして、一般質問を行います。
    ◯市長(白石正雄君) 青木議員の御質問にお答えいたします。

行頭マーカーは ◯ ○ 〇 ● のいずれにも対応する。
"""

from __future__ import annotations

import os
import re
import unicodedata
from dataclasses import dataclass, field
from html.parser import HTMLParser

SPEAKER_MARKERS = "◯○〇●"

# 例: ◯議長(山川太郎君) / ◯１２番(青木一郎君) / ◯市長(白石正雄君)
_SPEAKER_RE = re.compile(
    rf"^[{SPEAKER_MARKERS}]\s*(?P<title>[^\s(（]*)\s*[（(](?P<name>[^)）]+)[)）]\s*(?P<rest>.*)$"
)
# 例: ◯山川太郎議長 / ◯青木一郎議員 (肩書きが後置されるパターン)
_SPEAKER_POSTFIX_RE = re.compile(
    rf"^[{SPEAKER_MARKERS}]\s*(?P<name>\S+?)(?P<title>議長|副議長|議員|君)\s+(?P<rest>.*)$"
)

# 執行部とみなす肩書きのキーワード
_EXECUTIVE_KEYWORDS = (
    "市長",
    "副市長",
    "教育長",
    "部長",
    "局長",
    "課長",
    "次長",
    "参事",
    "会計管理者",
    "監査委員",
    "消防長",
    "選挙管理委員会",
    "農業委員会",
    "公営企業",
    "室長",
    "所長",
)

_HONORIFIC_RE = re.compile(r"(君|さん|議員)$")


@dataclass
class Utterance:
    """1回の発言。"""

    speaker: str          # 正規化した氏名
    title: str            # 肩書き(議長・◯番・市長 など、原文のまま)
    role: str             # "member" / "executive" / "chair" / "unknown"
    text: str             # 発言本文
    source: str           # 由来ファイル名

    @property
    def chars(self) -> int:
        return len(re.sub(r"\s", "", self.text))


@dataclass
class Minutes:
    """1ファイル分の会議録。"""

    source: str
    utterances: list[Utterance] = field(default_factory=list)

    @property
    def is_general_question(self) -> bool:
        """一般質問を含む会議録かどうか(本文に「一般質問」が現れるか)。"""
        return any("一般質問" in u.text for u in self.utterances)


class _TextExtractor(HTMLParser):
    """HTML会議録から本文テキストを取り出す簡易エクストラクタ。"""

    _SKIP_TAGS = {"script", "style", "head"}

    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag.lower() in self._SKIP_TAGS:
            self._skip_depth += 1
        elif tag.lower() in {"br", "p", "div", "tr", "li"}:
            self._chunks.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in self._SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._skip_depth == 0:
            self._chunks.append(data)

    def text(self) -> str:
        return "".join(self._chunks)


def html_to_text(html: str) -> str:
    parser = _TextExtractor()
    parser.feed(html)
    return parser.text()


def normalize_name(raw: str) -> str:
    """「青木 一郎君」→「青木一郎」のように氏名を正規化する。"""
    name = unicodedata.normalize("NFKC", raw)
    name = re.sub(r"\s+", "", name)
    name = _HONORIFIC_RE.sub("", name)
    return name


def classify_role(title: str) -> str:
    t = unicodedata.normalize("NFKC", title)
    if "議長" in t:  # 副議長も議事進行役として chair 扱い
        return "chair"
    if re.search(r"\d+番", t) or t == "議員":
        return "member"
    if any(k in t for k in _EXECUTIVE_KEYWORDS):
        return "executive"
    return "unknown"


def parse_text(text: str, source: str = "") -> Minutes:
    """会議録テキストを Minutes に変換する。"""
    minutes = Minutes(source=source)
    current: Utterance | None = None
    for line in text.splitlines():
        line = line.rstrip()
        m = _SPEAKER_RE.match(line) or _SPEAKER_POSTFIX_RE.match(line)
        if m:
            if current is not None:
                current.text = current.text.strip()
                minutes.utterances.append(current)
            title = unicodedata.normalize("NFKC", m.group("title") or "")
            # 後置パターンで title が「君」の場合、肩書き情報なし
            if title == "君":
                title = ""
            current = Utterance(
                speaker=normalize_name(m.group("name")),
                title=title,
                role=classify_role(title),
                text=m.group("rest") or "",
                source=source,
            )
        elif current is not None:
            current.text += "\n" + line
    if current is not None:
        current.text = current.text.strip()
        minutes.utterances.append(current)
    return minutes


def load_minutes_dir(path: str) -> list[Minutes]:
    """ディレクトリ内の .txt / .html 会議録をすべて読み込む。"""
    results: list[Minutes] = []
    for filename in sorted(os.listdir(path)):
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            continue
        lower = filename.lower()
        if lower.endswith((".html", ".htm")):
            with open(filepath, encoding="utf-8", errors="ignore") as f:
                text = html_to_text(f.read())
        elif lower.endswith(".txt"):
            with open(filepath, encoding="utf-8", errors="ignore") as f:
                text = f.read()
        else:
            continue
        minutes = parse_text(text, source=filename)
        if minutes.utterances:
            results.append(minutes)
    return results
