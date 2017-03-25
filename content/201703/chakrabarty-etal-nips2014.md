Title: Provable submodular minimization using Wolfe's algorithm
Date: 2017-03-25 00:00
Category: Optimization
Tags: [NIPS], 離散最適化, 劣モジュラ最小化

## 概要

劣モジュラ関数最小化問題で，実用上最速と噂されていたFujishige--Wolfeのアルゴリズム（最小ノルム点アルゴリズム）に擬多項式時間の保証を与えた論文．Fujishige--Wolfeは，基多面体 (base polyhedron) の上で2-ノルムの2乗が最小になる点を探すアルゴリズムである．


## 文献情報

* Author: D. Chakrabarty, P. Jain and P. Kothari
* Conference: NIPS
* Year: 2014
* [URL](https://papers.nips.cc/paper/5321-provable-submodular-minimization-using-wolfes-algorithm)

## コメント

1. Chakrabarty, et al. (2014) はまず，任意の多面体に対して，Wolfeの最小ノルム点アルゴリズムの連続最適化としての収束保証を与えた．次に，最小ノルム点の連続最適化としての近似精度が $\epsilon$ ならば，そこから構成できる解の（離散最適化としての）近似精度は $2n\epsilon$ である．よって，目的関数 $f$ の値のジャンプの最小幅 $F$ よりも $2n\epsilon$ を小さくとれば最適解となる．

1. 全体での計算量は $O((n^5 \gamma + n^7)F)$ になる．ただし，$\gamma$ は関数値オラクル呼び出しのコストである．ジャンプの幅 $F$ に依存しているため「擬」多項式時間である．ただし，$f$ が整数値であることが予めわかっていれば，ジャンプ幅は1で下から抑えればよい．

1. この分野の論文としては珍しく（？）計算機実験がある．強多項式時間アルゴリズムとしては2014年当時の理論最速だったIwata and Orlin (2009) のアルゴリズムと比較し，Fujishige--Wolfeの方が実計算時間が速い傾向にあることを示した．

1. 2017年現在，理論的に速いアルゴリズムは [Lee+2015] や [Chakrabarty+2017] とのことらしい．後者の筆頭著者はこの論文と同じ人．

#### 参考文献
* [Lee+2015] Lee, Sidford and Wong. Faster cutting plane method and its implications for combinatorial and convex optimization. In FOCS, 2015.
* [Chakrabarty+2017] Chakrabarty, Lee, Sidford and Wong. Subquadratic submodular function minimization. In STOC, 2017.
