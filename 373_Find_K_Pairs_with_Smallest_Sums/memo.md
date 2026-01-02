## Step1

- 配列が2つと数値kが与えられる、和が最も低い組み合わせをk個出力せよという問題
- シンプルに考える
  - nums1・nums2の全組み合わせをtupleに入れる
  - 組み合わせのtupleをkeyにして、和をvalueにしたdictをつくる
    - それか`(和, num1, num2)`のtuple配列でもいいかも
  - sortして、上位kのkeyを出力する
  - 計算量
    - 時間: O(N^2)
    - 空間: O(N^2) ※二次元配列を作っているため
    - これだとk = 10000で `Memory Limit Exceeded`となるので全列挙しない方法を考える必要がある

```py
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        combinations = []
        for num1 in nums1:
            for num2 in nums2:
                combinations.append([num1 + num2, num1, num2])

        combinations.sort()
        return [row[1:] for row in combinations[:k]]
```

- nums1/nums2のうち、最も小さい値を軸にして、その値が属していない方の配列を組み合わせ相手にしていくというのはどうか？
- nums1 and nums2 sorted in non-decreasing order
- 全部を走査する必要はなく、和が小さそうなものだけをチェックするイメージかな？
- 答えが出なかったのでここまでの思考を生成AIに渡し、回答してもらった
  - 一番最初のifいらない
  - 途中でswapしたりと頭で理解しづらいよくないコードな印象を受けた

```py
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        m, n = len(nums1), len(nums2)

        swapped = False
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
            swapped = True

        heap = []
        for i in range(min(k, m)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        res = []
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            a, b = nums1[i], nums2[j]
            res.append([b, a] if swapped else [a, b])

            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return res
```

- 少し計算量は悪くなるけど、可読性とのトレードオフを考えるとこっちの方がいいと思った
- `nums1[0], nums2[0]` の組み合わせが最小になるのは問題文の`nums1 and nums2 sorted in non-decreasing order`から自明なので、初期化という形でheapを宣言している
  - `nums2[0]`と`nums1`の要素の組み合わせをここでheapとして作っている
- res以下で残りの最小の組み合わせを作っている
  - 上の箇所で走査できなかった`nums2[j+1]`と`nums1`の組み合わせをheappushすることで見ている
  - 次のループでheappopされるので最小の組み合わせが取り出される
- 計算量
  - 時間: O(klogk), k * heappush(logk)
  - 空間: O(k)

```py
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i in range(min(k, len(nums1))):
            heappush(heap, (nums1[i] + nums2[0], i, 0))

        res = []
        while heap and len(res) < k:
            _, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heappush(
                    heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return res
```

## Step2

- https://github.com/yas-2023/leetcode_arai60/pull/10/files#diff-290402cd8493cb06a29272024b2ed9c39752fa597a928006c3bd1c76b7e8e66a
  - やっていることはstep1に書いたコードと変わりはなさそう？
  - 変数名の意味がわかりやすくよい

```
from heapq import heappush, heappop
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k_smallest_pairs = []
        heap = []
        max_rows = min(k, len(nums1))

        for row_index in range(max_rows):
            heappush(heap, (nums1[row_index]+nums2[0], row_index, 0))

        while heap and len(k_smallest_pairs) < k:
            _, row_index, column_index = heappop(heap)
            k_smallest_pairs.append((nums1[row_index], nums2[column_index]))
            if column_index + 1 < len(nums2):
                heappush(heap, (nums1[row_index] + nums2[column_index + 1], row_index, column_index + 1))

        return k_smallest_pairs
```