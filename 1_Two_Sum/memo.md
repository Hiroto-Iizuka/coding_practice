## Step1

- targetと現在の値との差分をdictに保持しておく
- その差分が登場した時点でreturnを返す
- 別のレビューでdictの命名規則は`key_to_value`がよいとご指摘いただいたので採用してみた（わかりやすい）
- 計算量
  - 時間: O(N)
  - 空間: O(N)

```py
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_index = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diff_to_index:
                return [diff_to_index[diff], i]
            else:
                diff_to_index[num] = i
```

## Step2

- `target - num`の変数名`complement`もいいかも
- dictの命名`num_to_index`としている人が多そう。
  - たしかにこっちのほうがよさそう（意味がそのまま通る） 
