## Step1

- 支柱に色を塗るパターンの数を出力する
- 隣り合う支柱に同じ色をつけるのは2つまで（3つ以上同じ色が並ぶのはダメ）
- DPとは「小さい問題を解いた結果が、大きい問題を解くのに何度も必要になるという性質」のことらしい
- 今回の問題だと、`same, diff = diff, (same + diff) * (k - 1)`の部分がそういうことみたい
- 時間計算量：O(N)
- 空間計算量：O(1)

```py
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def num_ways(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        
        same, diff = 0, k

        for i in range(2, n + 1):
            same, diff = diff, (same + diff) * (k - 1)

        return same + diff
```

## Step2

### 他の人のコードを見る
- https://github.com/naoto-iwase/leetcode/pull/35

いろいろな解き方を試されていて勉強になる

- https://github.com/naoto-iwase/leetcode/pull/35/changes#diff-c52fd179ae614e53682e0f0f57d5702672cbd03f0a4ef1c1e7b3c44f45e4f8faR84

[cache](https://docs.python.org/ja/3/library/functools.html#functools.cache)を使った解き方

- https://github.com/naoto-iwase/leetcode/pull/35/changes#diff-c52fd179ae614e53682e0f0f57d5702672cbd03f0a4ef1c1e7b3c44f45e4f8faR57-R80

今回の解法に近いが、合計の数だけを保持している
変数1つ分節約できるからこっちの方がいいのかなと思ったが、変数分けたほうがイメージしやすいかも

- https://github.com/naoto-iwase/leetcode/pull/35/changes#diff-c52fd179ae614e53682e0f0f57d5702672cbd03f0a4ef1c1e7b3c44f45e4f8faR115

時間計算量を節約できる解き方
書いてある通り実装重めなのでこの計算量が必要にならない限りは取りたくない手段だと思った
