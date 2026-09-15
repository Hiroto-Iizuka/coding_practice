https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

## Step1

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
- 買うタイミングも自由に決められる
- 一日に何度も売買できる
- 最大で１株まで保有できる
- `prices = [7,1,5,3,6,4]` のとき
  - 2日目に買い、3日目に売却（5-1=4）
  - 4日目に買い、5日目に売却（6-3=3）
  - 4+3=7となる
- `1 <= prices.length <= 3 * 104`
- `0 <= prices[i] <= 104`

### 回答

- 持っている状態と持っていない状態を管理する
- 時間計算量: O(n)
- 空間計算量: O(1)
- なにかしらの制約がある場合はこれでもいいけどやっていることはわかりづらくなった印象

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        not_hold = 0
        hold = -prices[0]

        for i in range(1, len(prices)):
            hold = max(hold, not_hold - prices[i])
            not_hold = max(not_hold, hold + prices[i])

        return not_hold
```

- 当日・翌日の差分が1以上なら足していき、合計値を返すといいらしい
- 時間計算量: O(n)
- 空間計算量: O(1)
- DPではないが、何をやっているかはわかりやすい

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]    

            if profit > 0:
                total_profit += profit

        return total_profit
```

## Step2
### 他の人のコードを読む

- https://github.com/h-masder/Arai60/pull/41/changes#diff-3d26e3b7d68dbe1856c4bbb6f8fb331c44570b0aa0ade1602f574df48672d807R77-R89

1つ目のやり方と同様。変数名など工夫があり読みやすくなっている。

- https://github.com/Manato110/LeetCode-arai60/pull/39/changes#diff-622f147294873187c9df36b2cb6b6d52197d3c9e783ba6433e1eba637e029197R107-R121

2つ目のやり方と同様。maxをつかわずに素直に書いている。

### コードの整形

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]    

            if profit > 0:
                total_profit += profit

        return total_profit
```
