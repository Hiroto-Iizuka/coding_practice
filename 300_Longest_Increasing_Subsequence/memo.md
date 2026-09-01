## Step1

- 最長の部分列の長さ（LIS, Longest Increasing Subsequence）を出力する
  - 元の配列順序が維持されること（ただし、要素を削除するのはOK）
  - 左から右に値が増加していること
- dp[i]: nums[i]で終わるLISの長さ
- 15分考えてわからないので答えを聞いた
  - DPはなぜかイメージが湧きづらく理解難しい気がしている。とりあえず計算途中のものをメモするイメージで考えている
- 時間計算量: O(n^2)
- 空間計算量: O(n)

```py
class Solution:
    def lengthOfLIS(nums):
        n = len(nums)
        if n == 0:
            return 0
        subsequences = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    subsequences[i] = max(subsequences[i], subsequences[j] + 1)
        return max(subsequences)
```

## Step2
### 他の人のコードを読む

- https://github.com/attractal/leetcode/pull/10/changes#diff-21337973a94d11dc1d61f52aade7995673de18528446051e69c520f5d521272bR39-R51

上のコードと似ているが、変数名が具体的で状態を想像しやすくて読みやすい気がする

- https://github.com/skypenguins/coding-practice/pull/50/changes#diff-0c860cd754249868513e4f9054206317fa33d0f548fc3896ac2b3e11822fd852R31-R32

コードではないけど、ここまで具体的に計算時間を出せるとよさそう

- https://github.com/naoto-iwase/leetcode/pull/37/changes

貪欲など、いろいろ書いているので参考までに。

### 

```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        subsequences = [1] * n
        
        for current_idx in range(1, n):
            for previous_idx in range(current_idx):
                if nums[current_idx] > nums[previous_idx]:
                    subsequences[current_idx] = max(subsequences[current_idx], subsequences[previous_idx] + 1)
                    
        return max(subsequences)
```
