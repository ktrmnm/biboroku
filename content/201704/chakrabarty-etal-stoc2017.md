Title: Subquadratic submodular function minimization
Date: 2017-04-02 00:00
Category: Optimization
Tags: [STOC], 離散最適化, 劣モジュラ最小化

## 概要

劣モジュラ関数最小化問題について：
(1) $O(n M^3 \log n EO)$ の偽多項式時間アルゴリズムを提案．ただし，目的関数は整数値で，最大値はMとする．
(2) $O(n^{5/3} EO/\epsilon) $ の $\epsilon$-近似アルゴリズムを提案．

アルゴリズムを一言でいえば，最小化したい関数のLovasz拡張を（確率的）劣勾配降下法で最小化する．
しかし，Lovasz拡張の劣勾配の更新が高速であるため，1ステップが速く回せる．
(1) の場合は，Lovasz拡張の劣勾配の成分の非ゼロ要素が O(M) であることに着目し，スパースベクトルの加算時に勾配を速く更新できるアルゴリズムを考える．
(2) の場合は，スパースな確率的劣勾配で分散が十分小さいものを高速に構成する．


## 文献情報

* Author: D. Chakrabarty, Y. Lee, A Sidford, and S. Wong
* Conference: STOC
* Year: 2017
* [arxiv](https://arxiv.org/abs/1610.09800)

## コメント

* 離散最適化を確率的凸最適化で殴った論文．近似アルゴリズムの方は構成が真に確率的なところが面白い．
