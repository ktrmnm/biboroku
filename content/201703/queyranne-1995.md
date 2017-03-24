Title: A combinatorial algorithm for minimizing symmetric submodular functions
Date: 2017-03-25 00:00
Category: Optimization
Tags: [SODA], 離散最適化, 劣モジュラ最小化

## 概要

対称劣モジュラ関数最小化の $O(|V|^3)$ アルゴリズムを与えた論文．ただし，対称劣モジュラ関数というのは，劣モジュラ関数 $f: 2^V \to \mathbb{R}$ であって，$f(X) = f(V - X)$ が成り立つものである．

## 文献情報

* Author: M. Queyranne
* Conference: SODA
* Year: 1995
* [URL](http://dl.acm.org/citation.cfm?id=313669)

## コメント

1. 対称劣モジュラ関数のわかりやすい例は，無向グラフのカット関数である．また，fが劣モジュラ関数のとき，$g(X) = f(X) + f(V - X)$ によって対称劣モジュラ関数 $g$ を作れる．

1. 「対称劣モジュラ関数最小化」とは，正確には，$|V| \geq 2$ として，空集合と全体集合を除いた $V$ の真部分集合の中で $f$ を最小化するものを求める問題である．例えば，非負重みをもつ無向グラフのカット関数の最小値は明らかに $f(\emptyset) = f(V) = 0$ であるが，そうではなくて非自明な部分の最小値を求める．

1. アルゴリズムの概要は次の通りである： まず，任意の対称劣モジュラ関数に対して，pendent pairと呼ばれる頂点のペア $(s,t)$ が存在することが知られている．ここでpendent pairというのは，$s$ を固定したとき，s-tカットの最小値が1点集合 $\{ t \}$ によって達成されるもののことである．このようなペアは $O(n^2)$ 回の関数呼び出しで発見することができる．Queyranneのアルゴリズムは，pendent pair発見アルゴリズムを再帰的に $n-1$ 回呼び出すことで得られる．定義から，pendent pair $(s, t)$ があるとき，最小化問題の解 $X$ は $f(X) = f(t)$ であるか，$s, t \in X$ であるかのどちらかである．前者であれば終了だが，それは判定できないので，ひとまず $t$ と $f(t)$ の値を記憶しておく．後者であると仮定すると，$(s, t)$ をまとめて1頂点だと思うことで，サイズが $n-1$ の問題に帰着される．よって，「pendent pairを見つけて結合する」という操作を残り2頂点になるまで繰り返せば，記憶した $t$ のうちどれかがminimizerになっている．

1. もともと，Nagamochi and Ibaraki (1992)の最小s-tカットアルゴリズムというものがあり，その拡張として提案されたらしい．[Fujishige (2005)](https://www.elsevier.com/books/submodular-functions-and-optimization/fujishige/978-0-444-52086-9) のsection 13にも歴史が載っている．
