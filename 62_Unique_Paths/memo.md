## Step1

### 問題の整理
- m * n のグリッド上でスタート地点（`grid[0][0]`）からゴール地点（`grid[m - 1][n - 1]`）に移動する
- 右か下にしか動けない
- ゴール地点に到達するすべての経路の数を返す

### DFSとカウントアップで実装自体はできるがTLEするコード

DFSとカウントアップでできるのではとパッと思いついたが、m,nの増加に対して、i,jを何度も計算し直すためTLEする

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)
```

### メモを使う

- 時間計算量: O(mn)
- 空間計算量: O(mn)

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {}
        return self.dfs(0, 0, m, n)

    def dfs(self, i, j, m, n):
        if i == m - 1 and j == n - 1:
            return 1
        if i >= m or j >= n:
            return 0
        if (i, j) in self.memo:
            return self.memo[(i, j)]

        self.memo[(i, j)] = self.dfs(i + 1, j, m, n) + self.dfs(i, j + 1, m, n)

        return self.memo[(i, j)]
```

- もっと効率的な解き方
- 時間計算量: O(mn)
- 空間計算量: O(n)

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]

        return row[-1]
```

## Step2

### 他の人のコードを読む

- https://github.com/MA-yo-TA/leetcode/pull/32/changes#diff-170566b52c2aec55cdb9c8ebd7669bfb336f9af9d385a8ad11aa657d6605a36cR9-R10
- https://github.com/MA-yo-TA/leetcode/pull/32/changes#diff-170566b52c2aec55cdb9c8ebd7669bfb336f9af9d385a8ad11aa657d6605a36cR29-R36
- https://github.com/Manato110/LeetCode-arai60/pull/34/changes#diff-e58d09796d15437a04b783849db77e2de471795065ed35dd4295a05ccd89d9afR7

数学でよくある設定らしい。
一度数学を学びなおしたほうがいいのかなー
`math.comb((m+n-2), m-1)`が計算量的にも一番有利らしい。素直にこれ使ったほうがいい気がした。combをどうやりますか、というのを問われているのかな

- https://github.com/kazuki-official/leetcode/blob/62-unique-paths/memo.md#code2-1-dp

AIで解説しながらだったけど、本来こういうのを経てやるのかもしれない。

### コードの整形

計算量的にはmath.combを実装するのが正しそう。
あえてDPを使うなら、少しでも計算量を節約するために m,nの短い方を配列長に使うように処理を入れるとよさそう

```py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m

        row = [1] * m

        for _ in range(1, n):
            for j in range(1, m):
                row[j] += row[j - 1]
                
        return row[-1]
```
