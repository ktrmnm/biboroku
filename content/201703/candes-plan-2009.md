Title: Near-ideal model selection by $\ell_1$ minimization
Date: 2017-03-24 00:00
Category: Statistics
Tags: [AS], lasso, 高次元, スパース推定, モデル選択

## 概要

Lassoのサポートリカバリー性能の最適性について調べた論文．サポートリカバリーというのは，おおよそ回帰係数の非ゼロ成分の添字（と符号）を当てるという意味である．

この論文ではまず，次の3つの意味でlassoのサポートリカバリーの性能を評価する：
1. スパースな回帰係数 $\beta$ がランダムに出るモデル (generic S-sparse model) を考える．このとき，lassoは $X \beta$ の$\ell_2$ ノルムの意味でのよい近似を高確率で与える．(Theorem 1.2)
1. $\beta$ の非ゼロ要素の絶対値の下限がある制約を満たすとき，lassoは高確率で $\beta$ の非ゼロ成分の添字と符号を当てる．(= exact model recovery, Theorem 1.3)
1. Lassoは，スパースなモデルの中で，真の $X \beta$ を $\ell_2$ の意味で最もよく近似するものに対して，ある精度で自動的に追従する．(= model selection oracle inequality, Theorem 1.4)

次に，「lassoにとって難しい具体的な問題」として，三角級数展開の形で定数信号を近似する問題を考える．これによって，上記の3つの定理が本質的には改善不可能であるということを主張している．

## 文献情報

* Author: E. Candès and Y. Plan
* Journal: The Annals of Statistics
* Year: 2009
* [URL](https://projecteuclid.org/euclid.aos/1247663751)

## コメント

1. ノイズは分散既知のガウシアンとする．計画行列にはcoherence propertyという，列どうしの内積の上界の仮定をおく．

1. ある問題設定においてLassoが最適であるということを主張しているわけではなく，lassoにとって最適な性能保証はどういう形を調べる目的で反例を作っていると思われる．
