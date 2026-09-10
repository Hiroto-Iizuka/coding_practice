https://leetcode.com/problems/house-robber-ii/description/

## Step1

- 数値の要素が入った配列 nums が与えられる
- 連続した要素2件は選ばずに、合計の最大値を求める
- 最初と最後は隣り合っている
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

### 回答

- 最初と最後は隣り合う設定なので、先頭`nums[0]`を選ぶ場合は`nums[1]`と`nums[len(nums) - 1]`は選べない。
  - つまり、House Robberの回答を2回分（先頭を選ぶ/選ばない）実行して大きい方を出せばよい。
  - 先頭を選ぶ場合: `nums[2:len(nums) - 1]` （インデックス番号1とlen(nums) - 1は選べない）
  - 先頭を選ばない場合: `nums[1:]`（先頭以降を確認する）
- 時間計算量: O(n)
- 空間計算量: O(n)
  - `max_loot`は最大100なので問題ないはず

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        case1 = nums[0] + self.max_money(nums[2:n - 1])
        case2 = self.max_money(nums[1:])

        return max(case1, case2)

    def rob_line(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
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

## Step2
### 他の人のコードを読む

- https://github.com/Manato110/LeetCode-arai60/pull/37/changes#diff-0ada15169c1bfbc855ba450fe39ac9bc5f80ec8f67e80356fce67b87aa72a6baR85

関数名 `max_robbed_money` としている
2パターンそれぞれの最大値という意味かな

- https://github.com/attractal/leetcode/pull/26/changes#diff-0ada15169c1bfbc855ba450fe39ac9bc5f80ec8f67e80356fce67b87aa72a6baR62-R89

再帰・cacheパターン。
コード自体には問題ないが、やはり再帰はループごとの状態が理解しづらいと感じる
`compute_max_amount(i)` が複数回呼び出されるため、キャッシュすることで効率的に計算できるということらしい

### 自分のコードを整形する

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        case1 = nums[0] + self.max_money(nums[2:n - 1])
        case2 = self.max_money(nums[1:])

        return max(case1, case2)
        
    def max_money(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
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
