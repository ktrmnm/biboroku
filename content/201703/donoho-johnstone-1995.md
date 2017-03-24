Title: Adapting to unknown smoothness via wavelet shrinkage
Date: 2017-03-19 22:20
Category: Statistics
Tags: [JASA], wavelet, SURE, minimax

## 概要

i.i.d.ガウス雑音が乗った信号を等間隔に観測して，平均二乗誤差の意味で雑音除去を行う問題を考える．真の信号 $f$ はSobolev空間（またはより一般にBesov空間）の球に含まれているが，微分可能性のパラメータ $m$ および球の半径 $C$ はわからないものとする．このような状況で，仮に滑らかさのパラメータを知っていた場合のミニマックス最適に近くなるような推定量を構成したい．

この論文では，SureShrinkという手法を提案している．SUREとはStein's Unbiased Risk Estimateの略であり，SUREに基づいて縮小 (shrinkage) のパラメータを決めるのでこのような名前である．

## 文献情報

* Author: D. Donoho and I. Johnstone
* Journal: Journal of The American Statistical Association
* Year: 1995
* [URL](https://www.jstor.org/stable/2291512)

## コメント

1. L^2-Sobolev球で滑らかさパラメータ（mとC）を知っている場合は，Pinsker推定量という線形推定量でミニマックスが達成される．Pinsker推定量はmとCに依存した構成になっているが，これらを知らなくても，知っていた場合のミニマックスリスクに自動追従したい（＝適応的ミニマックス）．Efromovich and Pinsker (1984) やNussbaum and Golubev (1990) の推定量などは適応的ミニマックスであることが知られている．

1. L^p-Sobolev球 (p < 2)の場合，そもそもmとCを知っている状況でも，線形推定量ではミニマックスが達成できないことが知られている．そこで，より広い意味の滑らかさを含みうる状況（Besov球）で適応的ミニマックスな推定量はどうやって作ればよいか，というのが本論文の理論的な背景である．
