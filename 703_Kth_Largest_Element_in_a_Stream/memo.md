## Step1

- Heapってなに？
  - 先頭の値を参照することで、最大値・最小値をO(N)で取得できるデータ構造
    - 保証されるのは先頭だけ
  - PythonだとList形式で表現される
  - `heapq.heapify(nums)`することで最小値が一番先頭に持っていかれる
  - k番目の最小値を取得したい場合、`len(nums) - k`回`heappop`することで`heap[0]=k番目`の最小値が取得できる
- 本質的な閃き方ではないけどカテゴリがHeapなのでそれで解くのかな
  - k番目に高いscoreを取得する
  - heapqには`heapify()`がある（min heap）
    - ※max heapとして使うにはListの正負反転が必要（今回は使わないが）
    - 最小の値を`heappop`で取り除くことで最大~k番目の値まで残すことができる、なので最小ヒープにしておく必要がある
    - なぜか最大ヒープで最大値を一番上に持ってきてk番目を取得することに執着してしまってた
      - これはヒープとソートしたListをごっちゃになっていたため
- 9ms、速い！
  - heapify（最小値の取り出し）: O(log N)
  - heappush: O(log N)

```py
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
```


- 配列を毎回降順にソートする手段もあり？
  - 何も捻らずにそのまま実装
    - 1500ms、addのたびにsortを実行するためめっちゃ遅い
    - sort: O(N log N)
```py
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]
```

- heapq
  - heappush: https://github.com/python/cpython/blob/3.14/Lib/heapq.py#L133
  - heappop: https://github.com/python/cpython/blob/3.14/Lib/heapq.py#L138

## Step2

- ちょっとしたことだが、heapqを毎回書くのは冗長なのでimportした

```py
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]
```

- https://github.com/mamo3gr/arai60/pull/8/files#diff-b8e64c318a6b5e40aba6edf4197cecfbe0b3849969675008085b46a2ab3aee21
  - `__init__`内で`self.top_k_ascending`をheapifyしているのはなぜだろう？空配列だから不要？
  - `while len(self.heap) > self.k`の重複を避けられるのはクールだなと思った
  - 自分のコードではaddでは`if`を使っている。これはaddされるのは1つの値だけだと決まっているから。なので共通化してwhileを使うのは少し抵抗がある（個人的なイメージ：if: 単一の値を検証、while: ループが必要な場合の検証）

```py
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_ascending = []
        heapq.heapify(self.top_k_ascending)
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k_ascending, val)
        while len(self.top_k_ascending) > self.k:
            heapq.heappop(self.top_k_ascending)
        return self.top_k_ascending[0]
```

- https://github.com/Yuto729/LeetCode_arai60/pull/14/files
  - `nums`のままはわかりづらいから`top_k_values`という名前にしているみたい
    - heap理解の途中でk番目までの値を入れておくところと理解したので`top_k_values`はよさそう。
    