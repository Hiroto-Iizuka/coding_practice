https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

## Step1

- `prices = [7,1,5,3,6,4]` のような配列が渡される
- 株を買った後に売って、最大となる利益を求める
- 利益が得られない場合は0を返す
- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

### 回答: TLE

- dpで管理するもの: `dp[購入日] = 最大の利益` とかどうだろう
  - iを購入日として、以下のように入れる
    - `max_profits[i] = prices[売却日] - prices[購入日]`
  - 事前に利益を計算（`profit = prices[j] - prices[i]`）し、0以下なら0としておく
  - 既存の`max_profits[i]`の値か、今回の利益をmaxで入れる（`max_profits[i] = max(prices[j] - prices[i], max_profits[i])`）
- この方法だと`1 <= prices.length <= 105`なので、最大 `10^5 * 10^5 = 10^10`になりTLEになる
  - そして、profitを何度も上書きする感じも好みではない
- 時間計算量: O(n^2)
- 空間計算量: O(n)

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profits = []
        for i in range(len(prices)):
            max_profits.append(0)
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit < 0:
                    profit = 0
                max_profits[i] = max(profit, max_profits[i])

        return max(max_profits)
```

### 回答

- 最安値とこれまでの最大利益を保存する方針
- 時間計算量: O(n)
- 空間計算量: O(1)

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit
```

## Step2
### 他の人のコードを読む

- https://github.com/MA-yo-TA/leetcode/pull/36/changes#diff-f9d1d3202402d3d800b455074f0d62fa57fb71eae0e2ab09c516f416eb5b8d04R3

`min_price`の初期値は`float("inf")`がよさそうとも思ったが、[この考え](https://github.com/tsadamor/Leetcode/pull/8/changes#diff-0c860cd754249868513e4f9054206317fa33d0f548fc3896ac2b3e11822fd852R53)と同じなので、`prices[0]`のままとしておく

- https://github.com/MA-yo-TA/leetcode/pull/36/changes#diff-c2253414b61972ac6a0ee75d992545be5642ed763c2a08289ba592abbfd085e9R11-R27

- https://github.com/MA-yo-TA/leetcode/pull/36/changes#diff-ff06b08ac44438356a5e1bab8d4b9b8e78a2a8f222cdea0a1b2e97db8869df99R1-R13

関数型っぽい書き方

- https://github.com/kazuki-official/leetcode/pull/37/changes#diff-0c860cd754249868513e4f9054206317fa33d0f548fc3896ac2b3e11822fd852R109-R147

recursionの書き方も面白いと思ったが、ちょっと冗長な印象を受けた

- https://github.com/Manato110/LeetCode-arai60/pull/38/changes#diff-51a148e3b52594eafc6999c4517eed5eb2c8eb1eeaa6f0a711ef9fdca11d3122R6

>問題的にはセーフかもしれないが、未来の情報を見るのは現実の株の考えに合っていないので、したくない  

そうそう、実務的に考えると未来の情報は見れないのでこういう考えだなあ。

### 自分のコードを整形する

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit
```

## Step3
### レビュー内容を反映する

```py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit
```
