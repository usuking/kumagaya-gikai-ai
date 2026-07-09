#!/usr/bin/env python3
"""会議録から議員・議会の評価レポートを生成するCLI。

使い方(サンプルデータで試す場合):

    python run_evaluation.py --minutes data/sample_minutes \
        --members data/members.sample.json \
        --votes data/votes.sample.csv \
        -o reports

AI定性評価も行う場合(要: pip install anthropic, ANTHROPIC_API_KEY):

    python run_evaluation.py --minutes data/sample_minutes --ai -o reports
"""

from __future__ import annotations

import argparse
import os
import sys

from kumagikai import ai_eval
from kumagikai.metrics import compute_stats, load_members, load_votes
from kumagikai.parse import load_minutes_dir
from kumagikai.report import write_reports


def main() -> int:
    parser = argparse.ArgumentParser(description="議員・議会評価レポート生成")
    parser.add_argument("--minutes", required=True, help="会議録(.txt/.html)のディレクトリ")
    parser.add_argument("--members", help="議員名簿JSON(任意)")
    parser.add_argument("--votes", help="賛否CSV(任意)")
    parser.add_argument("-o", "--output", default="reports", help="レポート出力先")
    parser.add_argument("--ai", action="store_true", help="Claude APIによる定性評価を行う")
    parser.add_argument(
        "--model", default=ai_eval.DEFAULT_MODEL, help=f"AI評価に使うモデル(既定: {ai_eval.DEFAULT_MODEL})"
    )
    parser.add_argument(
        "--min-chars",
        type=int,
        default=400,
        help="AI評価の対象とする最低発言文字数(既定: 400)",
    )
    args = parser.parse_args()

    minutes_list = load_minutes_dir(args.minutes)
    if not minutes_list:
        print(f"エラー: {args.minutes} に解析可能な会議録が見つかりません", file=sys.stderr)
        return 1
    print(f"会議録 {len(minutes_list)} 件を解析しました")

    roster = load_members(args.members) if args.members else None
    votes = load_votes(args.votes) if args.votes else None
    members, council = compute_stats(minutes_list, roster=roster, votes=votes)
    print(f"議員 {len(members)} 名の発言を集計しました(発言あり: {council.speaking_members} 名)")

    member_evals: dict[str, dict] = {}
    council_eval = None
    if args.ai:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            print(
                "警告: ANTHROPIC_API_KEY が未設定です。AI評価をスキップします "
                "(anthropic SDK のプロファイル認証がある場合はこの警告を無視して続行します)",
                file=sys.stderr,
            )
        try:
            client = ai_eval._client()
            for name, stats in members.items():
                if stats.total_chars < args.min_chars:
                    print(f"  {name}: 発言が少ないためAI評価をスキップ")
                    continue
                print(f"  {name}: AI評価中...")
                member_evals[name] = ai_eval.evaluate_member(
                    name, stats.texts, model=args.model, client=client
                )
            print("  議会全体: AI評価中...")
            full_texts = [
                "\n".join(f"◯{u.title}({u.speaker}) {u.text}" for u in m.utterances)
                for m in minutes_list
            ]
            council_eval = ai_eval.evaluate_council(
                full_texts, model=args.model, client=client
            )
        except Exception as exc:  # noqa: BLE001
            print(f"AI評価でエラーが発生したため定量レポートのみ出力します: {exc}", file=sys.stderr)

    written = write_reports(
        members,
        council,
        args.output,
        member_evals=member_evals,
        council_eval=council_eval,
    )
    print(f"レポート {len(written)} 件を {args.output}/ に出力しました")
    print(f"  メイン: {written[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
