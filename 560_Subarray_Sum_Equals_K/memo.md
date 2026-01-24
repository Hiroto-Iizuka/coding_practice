## Step1

- Two Sumに似ているような気がする
- 部分配列：元の配列から連続した要素を取り出して作られるより小さい配列
- numsは昇順になっているのだろうか？
  - 累積和というアルゴリズムを知ってこれは関係ないとわかった
- と、考えても解法を全然思いつけないので答えを見る
- 累積和を使う


- TLEしている
  - O(N^2)となっているから？
  - でも最大でも`2 * 10^4`なのでせいぜい数万回な気がするけどTLEなんだ、厳しい
```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1

        return count
```

- 以下の答えを見た
  - cumsumが何の略かわからなかったけど、GPTによるとcumulative sum（累積和） の略っぽい
  - 累積和とは、先頭から現在の位置の値を足したものという意味
  - 読んでいるがなにをしているかよくわからない
  - なにがわからないかを考えてみる
    - `if total - k in cumsum_to_freq:`によってなにができるのかがわかっていない
      - 「過去に total - k という累積和が存在したか？」を確認している
    - 累積和と頻度という結びつきが直感的に理解できないのかも
```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        cumsum_to_freq = defaultdict(int)
        cumsum_to_freq[0] = 1
        for num in nums:
            total += num
            # 以下はcumsum_to_freq.get(total - k, 0)というようにも書ける
            if total - k in cumsum_to_freq:
                count += cumsum_to_freq[total - k]

            cumsum_to_freq[total] += 1

        return count
```

### 累積和（Prefix Sum）

- `[a, b, c, d]` -> `[0, a, a+b, a+b+c, a+b+c+d]`
  - これを記録しておくことで任意の区間での和をO(1)で計算できる
  - `nums[i] - nums[j + 1]`で i番目からj番目までの和を求めることができる

## Step2

- わからない点を明確にして、生成AIにつくってもらった上で少し変数名を変更した
- だいぶ何をやっているかがわかりやすくなったと思う

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1

        prefix_sum = 0
        answer = 0

        for num in nums:
            prefix_sum += num
            answer += prefix_sum_to_count[prefix_sum - k]
            prefix_sum_to_count[prefix_sum] += 1

        return answer
```

## Step3

- 指摘いただいた箇所を反映、少し簡潔になった
- https://github.com/Hiroto-Iizuka/coding_practice/pull/16#discussion_r2679850144
  - 鉄道があって、各駅間ごとの標高差が与えられる。標高差がちょうどKであるようなすべての駅の組み合わせを列挙する。
  - 以下のようになるらしい

```py
from typing import List
from collections import defaultdict

class Solution:
    def findStationPairs(self, elevationDiffs: List[int], k: int) -> List[List[int]]:
        result = []

        elevations = [0]
        for diff in elevationDiffs:
            elevations.append(elevations[-1] + diff)
        
        elevation_map = defaultdict(list)
        
        for i, elev in enumerate(elevations):
            target = elev - k
            if target in elevation_map:
                for j in elevation_map[target]:
                    result.append([j, i])
            
            elevation_map[elev].append(i)
        
        return result
```
