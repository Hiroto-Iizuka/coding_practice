## Step1

- 上位kまでの出現頻度の数値を配列で返す
- 出現頻度はdict, tupleあたりで管理できそう
- `[(1, 3), (2, 2), (3, 1)]`のような形式にする
- heapifyで上記をheap化できる？
- 取り出し時は元の数値のみを取り出してresultに追加する
- 途中経過はよさそうだけど出力が合わない
  - `result.append()`で意図しない動きになっている
  - いろいろ考えているうちに複雑かつ合わない実装になってしまったので、これを元に生成AIで答え合わせした

```py
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq = defaultdict(int)
        numbers = list(set(nums))
        for num in numbers:
            count = nums.count(num)
            freq[count] = num

        freq_heap = list(freq.items())
        heapify(freq_heap)

        while len(freq_heap) > k:
            heappop(freq_heap)

        result = []
        for freq in freq_heap:
            result.append(freq[1])

        return result
```

- 一応これでAC
  - でも意外と遅い 18ms
  - 時間計算量: O(N^2)
  - 空間計算量: O(N)

```py
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq = []
        for num in set(nums):
            count = nums.count(num)
            freq.append((count, num))

        heapify(freq)

        while len(freq) > k:
            heappop(freq)

        return [num for freq, num in freq]
```

- heapを使わない回答が一番最初に浮かんだ
  - おそい。18ms
  - 計算量
    - 時間: O(Nk) `for _ in range`の中で`max()`している
    - 空間: 
```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        result = []
        for _ in range(k):
            target = max(freq, key=freq.get)
            result.append(target)
            del freq[target]

        return result
```

- 上のパターンを改善した
  - maxではなく、事前にsortしておく
  - これは普通の速度 5ms
  - 計算量
    - 時間: O(N logN) sortedしているので
    - 空間: O(N)

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq_dic = defaultdict(int)
        for num in nums:
            freq_dic[num] += 1
        
        freq_ranking = sorted(freq_dic.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(freq_ranking[i][0])
        return result
```

- https://docs.python.org/3.11/library/collections.html#collections.Counter.most_common を使えばすぐできそうだけど、問題の意図ではないと思った
  - コードの中身自体は読んでおく
  - あ、これもheapq.nlargest使っている
  - 最終コードは結局これを実装しているってことかも
  - これを実装してみるという趣旨の問題だったのかな

```py
    def most_common(self, n=None):
        '''List the n most common elements and their counts from the most
        common to the least.  If n is None, then list all element counts.

        >>> Counter('abracadabra').most_common(3)
        [('a', 5), ('b', 2), ('r', 2)]

        '''
        # Emulate Bag.sortedByCount from Smalltalk
        if n is None:
            return sorted(self.items(), key=_itemgetter(1), reverse=True)

        # Lazy import to speedup Python startup time
        global heapq
        if heapq is None:
            import heapq

        return heapq.nlargest(n, self.items(), key=_itemgetter(1))
``` 

## Step2

  - [ここ](https://github.com/mamo3gr/arai60/pull/9/files)で調べていただいているので中身だけ見ておく
  - シンプル&速い 3ms

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
        return [num for num, count in freq.most_common(k)]
```

  - [most_common](https://github.com/python/cpython/blob/main/Lib/collections/__init__.py#L625)
    - `heapq.nlargest`という関数があるのか

```py
if n is None:
  return sorted(self.items(), key=_itemgetter(1), reverse=True)

# Lazy import to speedup Python startup time
global heapq
if heapq is None:
    import heapq

return heapq.nlargest(n, self.items(), key=_itemgetter(1))
```

- 自分の回答と似ているけど、sortのkeyが異なる解法
  - `数値: 頻度`をtuple化して頻度で並び替えたけど、tuple化せずにdictのままできるのか、イイ
  - しかも速い、4ms

```py
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        for n in nums:
            num_count[n] += 1

        nums_frequent_order = sorted(num_count, key=num_count.get, reverse=True)
        return nums_frequent_order[:k]
```

## Step3

- heapを使ったパターンのレビューを反映してみる

```py
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = []

        for num in set(nums):
            count = nums.count(num)
            frequency.append((count, num))

        heapq.heapify(frequency)

        while len(frequency) > k:
            heapq.heappop(frequency)

        return [num for _, num in frequency]
```

- dictを使った方法をリファクタ、だいぶ簡潔で読みやすい
  - `nlargest(n, iterable, key=None)`
    - https://github.com/python/cpython/blob/3.14/Lib/heapq.py#L537
    - https://docs.python.org/ja/3/library/heapq.html#heapq.nlargest
    - iterableのデータセットのうち、最大値から降順にn個の値のリストを返す。まさに今回の要件を満たすメソッド
  - dictの変数名をkey_to_value形式に変更

```py
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = collections.defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1
        
        return heapq.nlargest(k, num_to_frequency, key=num_to_frequency.get)
```