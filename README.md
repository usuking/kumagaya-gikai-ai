# kumagaya-gikai-ai

熊谷市議会の公開情報(会議録・議員名簿・審議結果)をもとに、
**議員個人の議会活動**と**議会全体の審議**を定量+AI定性で評価するツール群です。

> 評価は公開情報に基づく参考資料であり、議員個人の人格・能力を断定するものではありません。
> 基準・方法論・限界は [docs/evaluation_criteria.md](docs/evaluation_criteria.md) を必ず参照してください。

## 構成

```
fetch_minutes.py        会議録の取得(URL一覧 → テキスト保存)
download_minutes.py     リンク集ページからの一括ダウンロード(汎用)
run_evaluation.py       解析・評価・レポート生成のCLI
kumagikai/
  parse.py              会議録テキスト → 発言者別発言
  metrics.py            定量指標(発言量・一般質問・賛否・ジニ係数など)
  ai_eval.py            Claude APIによる定性評価(ルーブリック採点)
  report.py             Markdownレポート出力
docs/
  evaluation_criteria.md  評価基準・方法論・倫理的配慮
  data_sources.md         熊谷市議会の公開データの入手先
data/
  sample_minutes/         動作確認用の架空の会議録
  members.sample.json     名簿のサンプル(実名簿の形式見本)
  votes.sample.csv        賛否CSVのサンプル
```

## クイックスタート(サンプルデータ)

標準ライブラリのみで動作します(Python 3.9+)。

```bash
python run_evaluation.py \
  --minutes data/sample_minutes \
  --members data/members.sample.json \
  --votes data/votes.sample.csv \
  -o reports
```

`reports/council_report.md`(議会全体)と `reports/members/<氏名>.md`(議員別)が生成されます。

## 実データでの手順

1. **会議録の取得** — [会議録検索システム](https://www.city.kumagaya.lg.jp/shigikai/kagiroku.html)で
   対象会議の本文表示ページURLを集め、1行1件で `urls.txt` に保存して:

   ```bash
   python fetch_minutes.py --url-list urls.txt -o data/minutes
   ```

2. **議員名簿の作成** — [各種議員名簿](https://www.city.kumagaya.lg.jp/shigikai/meibo/kakushumeibo.html)の
   PDFを参照し、`data/members.sample.json` と同じ形式で `data/members.json` を作成。

3. **賛否の転記(任意)** — 定例会ごとの審議結果ページから
   `data/votes.sample.csv` と同じ形式で `data/votes.csv` を作成。

4. **評価の実行**:

   ```bash
   python run_evaluation.py --minutes data/minutes \
     --members data/members.json --votes data/votes.csv -o reports
   ```

## AIによる定性評価

会議録の発言を5基準(具体性・政策提案性・追及力・市民関連性・論点明確さ)で
ルーブリック採点し、根拠引用つきの所見を生成します。

```bash
pip install -r requirements.txt      # anthropic SDK
export ANTHROPIC_API_KEY=sk-ant-...
python run_evaluation.py --minutes data/minutes --members data/members.json --ai -o reports
```

- 既定モデルは `claude-opus-4-8`(`--model` で変更可)。
- APIキーやSDKが無い場合は自動的に定量評価のみにフォールバックします。
- AIスコアは「参考意見」です。公開前に人間が引用の正確さを確認してください。

## データ取得時の注意

対象サイトの利用規約・robots.txt に従ってください。`fetch_minutes.py` は
アクセス間隔を2秒空けます。取得したデータの出典は明示してください。
