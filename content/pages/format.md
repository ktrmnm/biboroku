Title: フォーマットガイド
Date: 2017-03-19 23:00
Slug: format-guide

### メタデータ

* `Title` 論文のタイトル
* `Date` 記入日
* `Category` 現状では用途が決まっていない．`Statistics` `ML` `Optimization` などの大まかな分類を記入
* `Tags` 研究分野の細目 (e.g. カーネル法，Deep Learning) や論文誌名・会議名 (e.g. [Biometrika], [NIPS], [arXiv]) を記入
* `Slug` URL生成用．なければタイトルから自動生成される

記入例

```Markdown
Title: Adapting to Unknown Smoothness via Wavelet Shrinkage
Date: 2017-03-19 22:20
Category: Statistics
Tags: [JASA], wavelet, SURE

```

### 本文フォーマット

基本的には論文の概要を書く。文献情報はなるべく正確であることが望ましいが、URLなどから復元できるならば省略する。

| 項目名 | 備考 |
| --- | --- |
| 概要 | 200字程度 |
| 文献情報 | 論文誌名などの略称 / 著者 / 出版年 / URL |
| 新規性・差分 | |
| 手法 | |
| 結果 | |
| コメント | |

項目は [@arXivTimes](https://github.com/arXivTimes/arXivTimes) さんのものを参考にした
