#!/usr/bin/env python3
"""熊谷市議会の会議録を取得してテキスト保存するスクリプト。

熊谷市議会の会議録は会議録検索システム(kaigiroku.net)で公開されている。
入口: https://www.city.kumagaya.lg.jp/shigikai/kagiroku.html

検索システムはJavaScriptアプリのため、全自動クロールではなく
「会議録表示ページのURL一覧を渡す」方式を基本とする:

  1. 会議録検索システムで対象の会議を検索し、本文表示ページのURLを集める
  2. URLを1行1件でテキストファイルに保存する
  3. 本スクリプトで一括ダウンロード・テキスト化する

     python fetch_minutes.py --url-list urls.txt -o data/minutes

単純なリンク集ページからの一括取得は download_minutes.py も利用できる。

> 取得の際は対象サイトの利用規約・robots.txt に従い、アクセス間隔を空けること。
"""

from __future__ import annotations

import argparse
import os
import re
import time
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from kumagikai.parse import html_to_text

USER_AGENT = "kumagaya-gikai-ai/0.1 (civic-tech; minutes archiver)"
REQUEST_INTERVAL_SEC = 2.0


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="ignore")


def safe_filename(url: str, index: int) -> str:
    path = urlparse(url).path.strip("/").replace("/", "_")
    base = re.sub(r"[^\w.-]", "_", path) or f"minutes_{index:03d}"
    if not base.endswith(".txt"):
        base += ".txt"
    return base


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--url-list",
        required=True,
        help="会議録本文ページのURLを1行1件で書いたテキストファイル",
    )
    parser.add_argument("-o", "--output", default="data/minutes", help="保存先ディレクトリ")
    args = parser.parse_args()

    with open(args.url_list, encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    os.makedirs(args.output, exist_ok=True)
    for i, url in enumerate(urls, start=1):
        try:
            body = fetch(url)
        except Exception as exc:  # noqa: BLE001 - 続行して残りを取得する
            print(f"[{i}/{len(urls)}] 取得失敗 {url}: {exc}")
            continue
        text = html_to_text(body) if "<html" in body.lower() else body
        dest = os.path.join(args.output, safe_filename(url, i))
        with open(dest, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"[{i}/{len(urls)}] {url} -> {dest}")
        if i < len(urls):
            time.sleep(REQUEST_INTERVAL_SEC)


if __name__ == "__main__":
    main()
