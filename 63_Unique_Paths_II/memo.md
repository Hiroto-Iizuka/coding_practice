https://leetcode.com/problems/unique-paths-ii/description/

## Step1

- Unique Pathsと同じように経路の数を返す
- 障害物が追加されており、`obstacleGrid: List[List[int]]` を渡される
  - `1` のgridは障害物なので経路に含められない

### DPの手順

1. DPで管理するもの: ある時点のマスまでの経路数
2. 漸化式: `dp[i][j] = dp[i-1][j]+dp[i][j-1]`
3. 最初の値: `dp[0][0] = 1` （スタート地点）

### 今回の回答

- 62. Unique Pathを参考に書いてみる
- `nums_path`をDPとして扱う。ある時点のマスまでの経路数を記録していく。最終要素が合計の経路数となる想定
- 障害物が存在するルートの時は`nums_path`のカウントに入れない方式
- 時間計算量: O(mn)
- 空間計算量: O(n)

```py
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row, column = len(obstacleGrid), len(obstacleGrid[0])
        nums_path = []
        for j, num in enumerate(obstacleGrid[0]):
            if num == 0 and (j == 0 or nums_path[j - 1] == 1):
                nums_path.append(1)
            else:
                nums_path.append(0)

        for i in range(1, row):
            for j in range(column):
                if obstacleGrid[i][j] == 1:
                    nums_path[j] = 0
                elif j > 0:
                    nums_path[j] += nums_path[j - 1]
        return nums_path[-1]
```

## Step2
### 他の人のコードを見る

- https://github.com/Manato110/LeetCode-arai60/pull/35/changes#diff-e69af139ee833685dd9f7a46a1a522e9fba655e19fd100a2a12b6eb807a78442R71-R72

障害物あり/なしを定数で書いている。わかりやすい

- https://github.com/Manato110/LeetCode-arai60/pull/35/changes#r3173660980

O(mn) -> O(n)に削減する話。参考になる

- https://github.com/mamo3gr/arai60/pull/32/changes

例外メッセージも書いてて実践的

- https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.qdbwc4eyd7p0

コメント集。


### 自分のコードを修正する

- 定数を取り入れた。（REACHABLE・BLOCKEDという単語にした）

```py
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        REACHABLE, BLOCKED = 1, 0

        row, column = len(obstacleGrid), len(obstacleGrid[0])
        nums_path = []
        for j, num in enumerate(obstacleGrid[0]):
            if num == 0 and (j == 0 or nums_path[j - 1] == REACHABLE):
                nums_path.append(REACHABLE)
            else:
                nums_path.append(BLOCKED)

        for i in range(1, row):
            for j in range(column):
                if obstacleGrid[i][j] == 1:
                    nums_path[j] = BLOCKED
                elif j > 0:
                    nums_path[j] += nums_path[j - 1]

        return nums_path[-1]
```