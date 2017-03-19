# biboroku: 論文備忘録

## 概要

* 論文を読んだ記録をMarkdown形式で管理するためのリポジトリ
* 主な対象分野: 統計学，機械学習，最適化手法，数学

## 基本フォーマット

* (書きかけ)
* 

## ドキュメントの生成について

### 使用ツール

* Python (3.6.0)
* [Pelican](https://github.com/getpelican/pelican) (>=3.7.1)
  * テーマ: [foundation-default-colours](https://github.com/getpelican/pelican-themes/tree/master/foundation-default-colours)

導入
`pip install pelican markdown`

### 執筆作業

HTMLの生成とローカルでの確認
```
make html
make serve
```

### gh-pagesブランチへのアップロード

```
make github
```
