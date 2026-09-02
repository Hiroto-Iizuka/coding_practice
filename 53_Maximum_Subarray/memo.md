## Step1

- 和が最大となる部分配列を返す
  - numsを順番に足していく
  - 足した場合と足さなかった場合とで大きい方をdpに保存する
- 生成AIにヒントもらいながらも解けた（20分）
- 時間計算量: O(n)
- 空間計算量: O(n)

```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sums = [0] * len(nums)
        subarray_sums[0] = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            subarray_sums[i] = max(nums[i] + subarray_sums[i - 1], nums[i])

        return max(subarray_sums)
```

## Step2 

- https://github.com/skypenguins/coding-practice/pull/34/changes#diff-0c860cd754249868513e4f9054206317fa33d0f548fc3896ac2b3e11822fd852R39-R43
- https://github.com/Manato110/LeetCode-arai60/pull/33/changes#diff-95305de1e9bf283c3d5bc14487393733af825dba9d588055983a75d4808d3ccaR74-R97

自分が書いた方法もkadane法というらしい。
SWEの常識に入る解き方を調べてみる

- https://github.com/Manato110/LeetCode-arai60/pull/33/changes#diff-95305de1e9bf283c3d5bc14487393733af825dba9d588055983a75d4808d3ccaR56-R69

このあたりがSWEの常識的な解き方だろうか？
累積和を使っているけど、本質的にはKadaneと同じような気がする

### 最終的な自分のコード（修正があれば反映）

```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sums = [0] * len(nums)
        subarray_sums[0] = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            subarray_sums[i] = max(nums[i] + subarray_sums[i - 1], nums[i])

        return max(subarray_sums)
```
