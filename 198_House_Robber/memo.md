https://leetcode.com/problems/house-robber/description/

## Step1

- 問題設定が物騒すぎる
- 数値の要素が入った配列 nums が与えられる
- 連続した要素2件は選ばずに、合計の最大値を求める
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

### 回答

- DPで管理すべきもの： そこまでの要素で得られる最大合計
- 漸化式の組み立てが思いつかないので生成AIに聞いた 
  - `dp[i] = max(dp[i-2] + nums[i], dp[i-1])`
  - その家で盗むかどうかを上記で選択している
    - 2つ前までの金額合計（dp[i-2]）と今回の家のお金の和と、前回までの家の金額合計（dp[i-1]）の大きい方
- 時間計算量: O(n)
  - forループが nums の要素数（n）に比例する回数だけ回るため
- 空間計算量: O(n)
  - max_loot が nums と同じ長さ（n）の配列を1つ持つため

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_loot = [0] * len(nums)

        for i in range(len(nums)):
            if i - 2 >= 0:
                prev2 = max_loot[i - 2]
            else:
                prev2 = 0

            if i - 1 >= 0:
                prev1 = max_loot[i - 1]
            else:
                prev1 = 0

            take = nums[i] + prev2
            skip = prev1

            max_loot[i] = max(take, skip)

        return max(max_loot)
```

## Step2
### 他の人のコードを見る

- https://github.com/h-masder/Arai60/pull/38/changes#diff-3c850a4f263e6a14e39bf7cdb36bc4d46d1cfa708b6e2163969d6e6bab75213dR72-R90

メモ化パターン
取り組みとしてなるべく既存ライブラリを使いたくないので参考までにしておく

- https://github.com/Manato110/LeetCode-arai60/pull/36/changes#diff-b1642025ab2067fabcdc6478da099c2a1970c91a2662b6643d92b263fd1dbd1bR5-R35

問題を式に落とし込んでいてわかりやすい

- https://github.com/attractal/leetcode/pull/24/changes#diff-b1642025ab2067fabcdc6478da099c2a1970c91a2662b6643d92b263fd1dbd1bR65-R76

みた中では自分のコードに一番近いか...？
このくらい短くのも良さそう

### コードを整える

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        max_loot = [0] * len(nums)

        for i in range(len(nums)):
            if i - 2 >= 0:
                prev2 = max_loot[i - 2]
            else:
                prev2 = 0

            if i - 1 >= 0:
                prev1 = max_loot[i - 1]
            else:
                prev1 = 0

            take = nums[i] + prev2
            skip = prev1

            max_loot[i] = max(take, skip)

        return max(max_loot)
```

## Step3
### レビュー内容を反映する

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        max_loot = [0] * len(nums)
        max_loot[0] = nums[0]
        max_loot[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            take = nums[i] + max_loot[i - 2]
            skip = max_loot[i - 1]

            max_loot[i] = max(take, skip)

        return max_loot[-1]
```