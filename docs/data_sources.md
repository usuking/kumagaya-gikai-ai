# 熊谷市議会 データソース一覧

評価に使う公開情報の入手先(2026年7月時点の調査)。

## 会議録

- **入口ページ**: 会議録検索(熊谷市公式)
  https://www.city.kumagaya.lg.jp/shigikai/kagiroku.html
- 検索システムは kaigiroku.net(会議録検索システム)を利用しており、
  昭和58年以降の定例会等の会議録を検索・閲覧できる(平成17年10月以降が新・熊谷市)。
- 検索システムはJavaScriptアプリのため、`fetch_minutes.py --url-list` に
  本文表示ページのURL一覧を渡してテキスト保存する運用を基本とする。

## 議員名簿・会派

- **各種議員名簿**(議員名簿・会派構成一覧表・委員会名簿、PDF)
  https://www.city.kumagaya.lg.jp/shigikai/meibo/kakushumeibo.html
- **議員紹介**
  https://www.city.kumagaya.lg.jp/shigikai/meibo/index.html
- 定数30。直近の一般選挙は2023年4月23日執行。2025年10月に補欠選挙が行われており、
  名簿は必ず最新のPDFで確認して `data/members.json` に反映すること。

## 議案・審議結果(賛否)

- **審議結果**(定例会ごとのページ。議案一覧と議員別賛否のPDFを掲載)
  例: https://www.city.kumagaya.lg.jp/shigikai/gaiyou/r7_12teireikai/kekka0712.html
  (「熊谷市議会 審議結果」で定例会ごとのページを検索)
- PDFから `data/votes.csv`(列: 議案番号,議案名,議員名,賛否)へ転記する。

## 選挙結果

- **熊谷市議会議員選挙(過去の結果)**
  https://www.city.kumagaya.lg.jp/about/soshiki/senkyo/senkyokanriiinkai/result/sigi-kekka.html
- 令和5年(2023年)一般選挙の開票結果PDF:
  https://www.city.kumagaya.lg.jp/about/soshiki/senkyo/senkyokanriiinkai/result/sigi-kekka.files/R5sigi-kaihyou.pdf

## その他

- **熊谷市議会トップ**: https://www.city.kumagaya.lg.jp/shigikai/index.html
- 埼玉県議会(北第4区=熊谷市選出)の情報は県議会サイトを参照(市議会評価の対象外)。

## 注意

- 取得の際は各サイトの利用規約・robots.txt に従い、アクセス間隔を空けること
  (`fetch_minutes.py` は2秒間隔でアクセスする)。
- 本リポジトリの `data/sample_minutes/`・`data/members.sample.json`・`data/votes.sample.csv` は
  パイプライン動作確認用の**架空データ**であり、実在の議員・議事とは無関係。
