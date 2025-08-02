# kumagaya-gikai-ai

このリポジトリには、地方議会の会議録をダウンロードするための簡易スクリプトが含まれています。

## 使い方

```bash
python download_minutes.py <index_page_url> -o <output_dir>
```

- `<index_page_url>`: 会議録へのリンクが掲載されているページのURL。
- `<output_dir>`: ダウンロードしたファイルを保存するディレクトリ。省略時は`minutes`ディレクトリに保存されます。

スクリプトはページ上のPDF/TXT/HTMLファイルへのリンクを解析し、リンク先のファイルを取得して指定ディレクトリに保存します。

## 例

```bash
python download_minutes.py https://example.com/kaigiroku/index.html -o data
```

> 実際の自治体サイトを利用する際は、サイト利用規約に従ってください。
