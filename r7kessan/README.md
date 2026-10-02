# r7kessan（令和7年度 熊谷市決算 傍聴用資料フォルダ）

令和8年9月定例会で審査される**令和7年度決算**を、議会の決算審査を傍聴しながら調べるための資料フォルダです。熊谷市が公開している議案資料・監査委員資料などのPDFから抽出したテキストと、「資料No.2の何ページか」をすぐ引くための索引を収めています。

**PDF本体はこのリポジトリに入れていません。** 原本は下記の元URL（`manifest.tsv` の `url` 列）から取得してください。

## 1. ファイル構成

| パス | 内容 |
|---|---|
| `事業索引_一般会計歳出.md` | 歳出の全事業（711件）を款→項→目の順に並べた索引。資料No.2の印刷ページ（事業名頁-金額頁）、予算現額・支出済額・翌年度繰越額・不用額、資料No.4 別表第14の頁と事業概要 |
| `歳入_款別索引.md` | 歳入の款・項ごとの資料No.2印刷ページ、予算現額、調定額、収入済額、不納欠損額、収入未済額 |
| `text/` | 収録PDF（60ファイル）を `pdftotext -layout` で抽出したテキスト。PDF 1頁 ＝ 改ページ文字（`\f`）区切り1つ |
| `manifest.tsv` | 収録60ファイルの一覧（区分・ファイル名・元URL・頁数・文字数・バイト数） |
| `README.md` | このファイル |

## 2. 資料番号と正式名称（令和8年9月定例会 市長提出議案 No.01〜No.18）

正式名称は熊谷市サイト「令和8年市長提出議案」ページ（https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.html）のリンク表記です。

| 資料No. | 正式名称 | 頁数 | text/ のファイル | 元URL |
|---|---|---:|---|---|
| No.01 | 令和7年度熊谷市一般会計・特別会計歳入歳出決算書 | 35 | `09月定例会_議案No01_令和7年度一般会計・特別会計歳入歳出決算書.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_01.pdf |
| No.02 | 令和7年度熊谷市一般会計歳入歳出決算事項別明細書 | 499 | `09月定例会_議案No02_令和7年度一般会計歳入歳出決算事項別明細書.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_02.pdf |
| No.03 | 令和7年度熊谷市特別会計歳入歳出決算事項別明細書 | 63 | `09月定例会_議案No03_令和7年度特別会計歳入歳出決算事項別明細書.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_03.pdf |
| No.04 | 令和7年度熊谷市一般会計・特別会計実質収支に関する調書／熊谷市財産に関する調書／熊谷市歳入歳出決算説明書 | 102 | `09月定例会_議案No04_令和7年度実質収支に関する調書・財産に関する調書・歳入歳出決算説明書.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_04.pdf |
| No.05 | 令和7年度熊谷市公営企業会計決算書 | 127 | `09月定例会_議案No05_令和7年度公営企業会計決算書.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_05.pdf |
| No.06 | 令和7年度健全化判断比率等の状況について | 4 | `09月定例会_議案No06_令和7年度健全化判断比率等の状況について.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_06.pdf |
| No.07 | 令和7年度熊谷市一般会計・特別会計歳入歳出決算ほか審査意見書 | 87 | `09月定例会_議案No07_令和7年度一般会計・特別会計歳入歳出決算ほか審査意見書（議案添付版）.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_07.pdf |
| No.08 | 令和7年度熊谷市公営企業会計決算審査意見書 | 79 | `09月定例会_議案No08_令和7年度公営企業会計決算審査意見書（議案添付版）.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_08.pdf |
| No.09 | 令和8年度教育委員会の事務に関する点検・評価報告書(令和7年度対象) | 148 | `09月定例会_議案No09_令和8年度教育委員会の事務に関する点検・評価報告書（令和7年度対象）.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_09.pdf |
| No.10 | 令和7年度債権の放棄について | 2 | `09月定例会_議案No10_令和7年度債権の放棄について.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_10.pdf |
| No.11 | 令和8年度熊谷市一般会計・特別会計補正予算書 | 11 | `09月定例会_議案No11_令和8年度一般会計・特別会計補正予算書（9月補正）.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_11-2.pdf |
| No.12 | 令和8年度熊谷市一般会計・特別会計補正予算に関する説明書 | 31 | `09月定例会_議案No12_令和8年度補正予算に関する説明書（9月補正）.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_12.pdf |
| No.13 | 令和8年(9月)第3回定例会議案 | 53 | `09月定例会_議案No13_令和8年第3回（9月）定例会議案.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_13.pdf |
| No.14 | 令和8年(9月)第3回定例会専決処分の報告 | 23 | `09月定例会_議案No14_令和8年第3回（9月）定例会専決処分の報告.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_14.pdf |
| No.15 | 令和8年度熊谷市一般会計歳入歳出予算分析表(補正第2号) | 13 | `09月定例会_議案No15_令和8年度一般会計歳入歳出予算分析表（補正第2号）.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_15.pdf |
| No.16 | 令和8年(9月)第3回定例会議案 参考資料 | 37 | `09月定例会_議案No16_令和8年第3回（9月）定例会議案参考資料.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_16.pdf |
| No.17 | （市サイトの一覧に掲載なし。欠番） | － | － | － |
| No.18 | 令和8年9月市議会定例会 提案理由(要旨) | 6 | `09月定例会_議案No18_令和8年9月定例会提案理由（要旨）.txt` | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_18.pdf |

- 決算審査でよく使うのは **No.2（一般会計の事項別明細書）**、**No.4（実質収支に関する調書・財産に関する調書・歳入歳出決算説明書。別表第14「一般会計施行事業概況表」を含む）**、**No.7（決算審査意見書）** です。No.1は款項別の決算書、No.3は特別会計の事項別明細書、No.5・No.8は公営企業会計です。
- No.11の元URLのファイル名は `R0809_11-2.pdf` です（市サイトに掲載されているURLのとおり）。
- 頁数はPDFの総頁数（表紙・目次等を含む）です。**印刷ページ番号とはずれます**（No.2・No.4とも PDFの頁番号 ＝ 印刷ページ＋2）。

## 3. 収録一覧（6月・3月定例会分、監査委員資料ほか）

上の9月定例会分（区分A）に加え、令和7年度決算の審査・確認の参考になる次の資料を収録しています（区分ごとの意味は表の下を参照）。6月・3月定例会のその他の議案（令和8年度予算・補正予算など）は収録していません。必要な場合は上記の市サイトの一覧ページを参照してください。

### 区分B 令和8年6月定例会 市長提出議案（令和7年度の繰越・外郭団体決算）

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 06月定例会_議案No05_令和7年度一般会計繰越明許費繰越計算書 | 5 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0806_05.pdf |
| 06月定例会_議案No06_令和7年度特別会計繰越明許費繰越計算書 | 3 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0806_06.pdf |
| 06月定例会_議案No07_令和7年度特別会計事故繰越し繰越計算書 | 3 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0806_07.pdf |
| 06月定例会_議案No08_令和7年度公営企業会計予算繰越計算書 | 6 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0806_08.pdf |
| 06月定例会_議案No09_令和7事業年度土地開発公社の決算について | 11 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0806_09.pdf |
| 06月定例会_議案No10_令和7年度文化振興財団の決算について | 13 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0806_10.pdf |
| 06月定例会_議案No11_令和7年度大里地域勤労者福祉サービスセンターの決算について | 22 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0806_11.pdf |

### 区分C 令和8年3月定例会 市長提出議案（令和7年度最終補正予算）

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 03月定例会_議案No05_令和7年度一般会計・特別会計補正予算書（最終補正） | 21 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0803_05.pdf |
| 03月定例会_議案No06_令和7年度一般会計・特別会計補正予算に関する説明書（最終補正） | 55 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0803_06.pdf |
| 03月定例会_議案No07_令和7年度水道事業会計補正予算書 | 17 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0803_07.pdf |
| 03月定例会_議案No17_令和7年度一般会計歳入歳出予算分析表（補正第7号） | 13 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0803_17.pdf |
| 03月定例会_議案No18_令和7年度一般会計歳入歳出予算分析表（補正第8号） | 13 | https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0803_18.pdf |

### 区分D 監査委員 決算審査意見書

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 監査委員_令和7年度一般会計・特別会計歳入歳出決算審査意見書・基金運用審査意見書・健全化判断比率等審査意見書（8月18日提出版） | 82 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/teisyutu.files/r7ippan.tokubetukaikei-ikennsyo.pdf |
| 監査委員_令和7年度公営企業会計決算審査意見書（8月18日提出版） | 77 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/teisyutu.files/r7koueikigyoukaikei-ikennsyo.pdf |

### 区分E 監査委員 令和7年度定期監査結果（参考）

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 監査委員_令和7年度定期監査結果_市民部（令和8年5月29日公表） | 7 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7shiminbu-kansakekka.pdf |
| 監査委員_令和7年度定期監査結果_市長公室（令和7年8月26日公表） | 4 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7sityoukousitu-kannsakekka.pdf |
| 監査委員_令和7年度定期監査結果_建設部（令和8年5月29日公表） | 6 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7kensetubu-kansakekka.pdf |
| 監査委員_令和7年度定期監査結果_消防本部（令和8年2月18日公表） | 5 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7kyoubouhonbu-kansakekka.pdf |
| 監査委員_令和7年度定期監査結果_環境部（令和7年11月20日公表） | 6 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7kankyoubu-kansakekka.pdf |
| 監査委員_令和7年度定期監査結果_監査委員事務局（令和8年5月29日公表） | 3 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7kansaiinzimukyoku-kansakekka.pdf |
| 監査委員_令和7年度定期監査結果_行政センター（令和8年2月18日公表） | 5 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7gyouseisenta-kansakekka.pdf |
| 監査委員_令和7年度定期監査結果_議会事務局（令和8年5月29日公表） | 3 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7gikaizimukyoku-kansakekka.pdf |
| 監査委員_令和7年度定期監査結果_農業委員会事務局（令和8年5月29日公表） | 4 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7nougyouiinkaizimukyoku-kansakekka.pdf |
| 監査委員_令和7年度定期監査結果_選挙管理委員会事務局（令和8年5月29日公表） | 3 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7senkyokanriiinkaizimukyoku-kansakekka.pdf |
| 監査委員_令和7年度財政援助団体等監査結果_コミュニティセンター指定管理者（令和8年5月29日公表） | 4 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r7kansakekka.files/r7zaiseienzyodantaitoukansakekka.pdf |
| 監査委員_令和8年度定期監査結果_都市整備部（令和8年8月24日公表） | 5 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakekka/r8kansakekka.files/r8toshiseibibu-kansakekka.pdf |
| 監査委員_令和8年度熊谷市監査計画 | 4 | https://www.city.kumagaya.lg.jp/about/soshiki/kansa/kansaiinjimukyoku/oshirase/kansakijyun.files/r8kansakeikaku.pdf |

### 区分F 財政状況

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 財政課_令和7年度の財政状況_一般会計執行状況（令和8年3月末現在） | 1 | https://www.city.kumagaya.lg.jp/about/zaisei/zaisei/R7zaiseijoukyou.files/reiwa7.pdf |
| 財政課_令和7年度上期の財政状況_一般会計執行状況（令和7年9月末現在） | 1 | https://www.city.kumagaya.lg.jp/about/zaisei/zaisei/R7kamiki.files/R7kamihanki.pdf |

### 区分G 事務事業評価・成果指標（参考）

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 企画課_事務事業評価の考えかたについて | 1 | https://www.city.kumagaya.lg.jp/about/soshiki/sogo/kikaku/sousin/gyouseihyouka.files/R7_kangaekata.pdf |
| 企画課_総合振興計画審議会R8.2.18_資料1_成果指標の実績値及び進捗状況一覧 | 5 | https://www.city.kumagaya.lg.jp/about/soshiki/sogo/kikaku/sousin/H21_sousin_sinngikai.files/R7kaigishiryou-01.pdf |
| 企画課_総合振興計画審議会R8.2.18_資料3_令和7年度事務事業評価（令和6年度実施事業）一覧表 | 24 | https://www.city.kumagaya.lg.jp/about/soshiki/sogo/kikaku/sousin/H21_sousin_sinngikai.files/R7kaigishiryou-03.pdf |

### 区分H 市議会（9月定例会 運営資料）

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 市議会_令和8年第3回（9月）定例会_一般質問通告一覧 | 5 | https://www.city.kumagaya.lg.jp/shigikai/gaiyou/reiwa8nenn9gatu/ippannsitumon.files/ippan.pdf |
| 市議会_令和8年第3回（9月）定例会_付託区分表 | 4 | https://www.city.kumagaya.lg.jp/shigikai/gaiyou/reiwa8nenn9gatu/hutakukubun.files/hutaku.pdf |
| 市議会_令和8年第3回（9月）定例会_審議日程 | 1 | https://www.city.kumagaya.lg.jp/shigikai/gaiyou/reiwa8nenn9gatu/sinnginittei.files/0809HP.pdf |
| 市議会_令和8年第3回（9月）定例会_審議結果（9月18日議決分） | 1 | https://www.city.kumagaya.lg.jp/shigikai/gaiyou/reiwa8nenn9gatu/sinngikekka.files/0809kekka.pdf |
| 市議会_令和8年第3回（9月）定例会_議員提出議案第9号 | 4 | https://www.city.kumagaya.lg.jp/shigikai/gaiyou/reiwa8nenn9gatu/giinteishutugian.files/0809gitei.pdf |
| 市議会_令和8年第4回（12月）定例会_審議日程（予定） | 1 | https://www.city.kumagaya.lg.jp/shigikai/gaiyou/reiwa8nenn12gatu/shinnginittei.files/0812yotei.pdf |

### 区分I 令和7年度当初予算（参考）

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 財政課_令和7年度当初予算_予算編成の考え方 | 8 | https://www.city.kumagaya.lg.jp/about/zaisei/yosantuite/yosangaiyo/0001.files/R7yosanhensei.pdf |
| 財政課_令和7年度当初予算_主要事業一覧表 | 18 | https://www.city.kumagaya.lg.jp/about/zaisei/yosantuite/yosangaiyo/0001.files/R7shuyouzigyou.pdf |
| 財政課_令和7年度当初予算_予算分析表 | 13 | https://www.city.kumagaya.lg.jp/about/zaisei/yosantuite/yosangaiyo/0001.files/R7bunsekihyou.pdf |

### 区分J 教育委員会 点検・評価報告書（公表版）

| ファイル（text/ の名前から .txt を除いたもの） | 頁数 | 元URL |
|---|---:|---|
| 教育委員会_令和8年度教育委員会の事務に関する点検・評価報告書（令和7年度対象）_公表版 | 146 | https://www.city.kumagaya.lg.jp/about/soshiki/kyoiku/kyoikusomu/oshirase/tenkennhyouka.files/R8tennkennhyouka.pdf |
| 教育委員会_令和8年度教育委員会の事務に関する点検・評価報告書（令和7年度対象）_概要版 | 10 | https://www.city.kumagaya.lg.jp/about/soshiki/kyoiku/kyoikusomu/oshirase/tenkennhyouka.files/R8tennkennhyoukagaiyou.pdf |

区分の意味：A＝9月定例会 市長提出議案（令和7年度決算関係）／B＝6月定例会（繰越計算書・外郭団体決算）／C＝3月定例会（令和7年度最終補正予算）／D＝監査委員 決算審査意見書（8月18日提出版）／E＝監査委員 定期監査結果（参考）／F＝財政課 財政状況／G＝企画課 事務事業評価・成果指標／H＝市議会 9月定例会運営資料／I＝令和7年度当初予算（参考）／J＝教育委員会 点検・評価報告書（公表版・概要版）。

## 4. 元URLとPDFの入手

- 全ファイルの元URLは `manifest.tsv` の `url` 列にあります。例：`curl -O https://www.city.kumagaya.lg.jp/about/gian/r08gikaisiryo.files/R0809_02.pdf`（No.2）。
- `text/` は上記PDFを2026年10月2日に取得して抽出したものです。市サイト側でPDFが差し替えられた場合は内容・ページがずれることがあります。
- 抽出し直す場合は `pdftotext -layout 元.pdf 出力.txt`。1頁だけ見るなら `pdftotext -f N -l N -layout 元.pdf -`（Nは**PDFの頁番号**。印刷ページ＋2）。

## 5. 検索のコツ

`pdftotext` 由来のため、**文字間に空白が入る**ことがあります（特に別表第14の事業内容欄は両端揃えのため「シティプ ロモ ーシ ョン」のようになる）。**grep は空白を除去して照合するか、`'スポーツ *振興'` のように空白を許容する正規表現で書いてください。**

```bash
# 1) 空白を許容する正規表現で書く
grep -n 'スポーツ *振興' text/09月定例会_議案No02_*.txt
grep -nE 'シ *テ *ィ *プ *ロ *モ *ー' text/09月定例会_議案No04_*.txt

# 2) 空白（半角・全角）を除去してから照合する
#    ※ tr -d ' 　' は全角文字をバイト単位で壊すので使わない。perl か、UTF-8ロケール指定の sed を使う
perl -CSD -pe 's/[ \x{3000}]//g' text/09月定例会_議案No04_*.txt | grep -n 'シティプロモーション動画'
LC_ALL=C.UTF-8 sed 's/[ 　]//g' text/09月定例会_議案No04_*.txt | grep -n 'シティプロモーション動画'

# 3) 金額で探し、PDFの頁番号→印刷ページに直す（No.2・No.4は 印刷ページ ＝ PDFの頁番号 － 2）
awk 'BEGIN{RS="\f"} /40,034,600/ {print "PDF頁", NR, "→ 印刷p.", NR-2}' text/09月定例会_議案No02_*.txt
```

- **事業名は行の途中で折り返されます**（No.2は「○ 荒川公園周／辺再整備事／業」のように2〜5行に分かれる）。そのため `grep '荒川公園周辺再整備事業'` ではヒットしません。**事業名の前半だけ**（`荒川公園周`）で探すか、空白と改行をすべて除去して次のようにします（この方法はNo.2向き。No.4は事業名の行の間に他の列の文字が入るため不可で、事業名の最初の行、例 `シティプロモー` で探してください）。
  ```bash
  perl -CSD -0777 -pe 's/[\s\x{3000}]//g' text/09月定例会_議案No02_*.txt | grep -o '荒川公園周辺再整備事業'
  ```
- 事業名は全角数字（「２０周年記念」）、事業内容の本文は半角数字（「20周年」）が混在します。両方で検索するか、正規化（NFKC）して照合してください。
- 事業名で探すなら、まず `事業索引_一般会計歳出.md` を検索するのが最短です（事業名は折り返しなし・空白なしで収録）。


## 6. 表崩れの注意点（pdftotext の限界）

1. **資料No.2の歳出・歳入は見開き構造**で、左頁（偶数頁）に「款・項・目・予算現額・事業名」、右頁（奇数頁）に「事業費の節・支出済額・翌年度繰越額・不用額・備考」があります。`pdftotext` は左右を別々の頁として出力するため、**事業名と金額の行対応が崩れます**。対応は、事業名（○ で始まる）の位置と右頁の合計行の位置（行の高さが一致）で取ります。
2. 左頁の「款・項・目」と予算現額は、その目・項・款が**始まる行にしか出ません**（頁ごとの繰り返し表示はありません）。事業の所属する款項目は、直前に出てきた款・項・目の行で決まります。各右頁の脚注（「第 2款 総務費 第 1項 総務管理費」）はその頁に出てくる款項の一覧です。
3. 右頁では、**事業の合計行（事業費・支出済額・繰越・不用額）が、その事業の節行より上**にあります。事業が頁の下端にあると、節の内訳は次の見開きの右頁の冒頭に続きます（索引の備考に「節の内訳は p.○ に続く」と記載）。合計行と節行は見た目が似ていますが、節行は行頭に節番号（例「12 委託料」）が付いています。
4. 目・項・款の合計行は、予算現額が左頁側にあるため、右頁には**支出済額以降の4列しか出ません**。
5. 右端の**備考欄の金額**（例：委託料の内訳）は、節の金額・支出済額と同じ行に並んで出るため、列を取り違えやすいです。備考の金額は節の内訳で、事業の支出済額ではありません。
6. **頁上部に単独で出ることがある数字**（例「134」）は印刷ページではありません（印刷ページ－2の値）。印刷ページは**頁の最下部**に出る単独の数字です。
7. **資料No.4 別表第14**（別表の印刷p.82〜p.100）は「事業名｜決算額｜財源内訳｜事業内容」の4列表で、事業名・事業内容が列幅で折り返され、財源が複数行にわたるため、1事業が数行に散らばります。また「（繰越明許分）」の行は事業内容欄が元の事業と結合されており、内容文が2行にまたがって分かれて出ます（例：クマＰＡＹ発行事業と同（繰越明許分））。
8. 歳入（p.4〜p.73）も同じ見開き構造です。節の区分（「現年課税分」「滞納繰越分」など）は左頁の右端にあります。△は負の値（例：△20,117）。

## 7. 索引の作り方と検証

- `pdftotext -bbox`（単語ごとの座標）で、左頁の「○ 事業名」と右頁の事業合計行を行の高さで対応づけ、款・項・目は左頁の見出し行から決めました。テキストの並び順だけでは取れないため、座標を使っています。
- 歳出：事業711件。全141目で「事業の合計＝目の予算現額・支出済額・翌年度繰越額・不用額」が一致し、全事業の合計が資料No.2の歳出合計（予算現額 92,461,692,598円／支出済額 83,221,328,306円／繰越明許費 4,460,991,540円／不用額 4,779,372,752円）と一致。全事業で 予算現額＝支出済額＋翌年度繰越額＋不用額。事業の款・項は、金額頁の脚注とも照合して一致。
- 資料No.4 別表第14：177事業を抽出し、No.2の事業名（正規化後）と金額（支出済額）で突合。**177件すべて一致（要確認 0件）**。別表に載らない事業は534件（別表は主な事業のみ）。
- 歳入：22款・40項。項の合計＝款、全款の合計＝歳入合計（予算現額・調定額・収入済額・不納欠損額・収入未済額）が一致。
- 事業概要（別表第14の内容を40字以内に要約）は、別表の内容欄を読んで書いた要約で、原文の引用ではありません。
- 款番号に注意：**第10款 教育費、第11款 公債費、第12款 予備費**です（公債費は第12款ではありません）。
- 全款（議会費〜予備費）を同じ方法で作成しており、優先款だけに絞った簡易版ではありません。

## 8. 利用上の注意

- 金額・頁は公開PDFから機械的に抽出して検算したものですが、**発言・引用の前には原本PDFで確認**してください。
- 目・節のレベル（例：委託料の額、目の合計）は索引に含めていません。事業の「金額頁」を開くと節別の金額と備考欄の内訳が見られます。
- 3桁カンマ付きの金額は円単位です。
