## Step1

- num1, num2の共通に登場する値を配列で出力する ※要素はユニーク
- 二重for文でやると以下の通り
- ただしかなり遅い 36ms
  - 計算量
    - 時間: O(N^2)
    - 空間: O(N)

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict(int)

        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    dic[num1] += 1
        
        return [int(key) for key in dic.keys()]
```

- nums1/nums2それぞれから重複を削除しておく（`set()`）

- dictに保存したほうがいいかなと思ったけど、setで十分だった
- これははやい 0msだった
  - 計算量
    - 時間: O(N)
    - 空間: O(N)

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        result = []
        for num2 in nums2_set:
            if num2 in nums1_set:
                result.append(num2)

        return result
```

- ※なんなら一行だった
  - https://github.com/mamo3gr/arai60/pull/13/files#diff-60cc9635c10d1d4ff1167c27af0e2ae79e126ad217c09e0eae8320540522519b
  - 出題意図じゃないのか、なるほど

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

## Step2

- intersection
  - Pythonの組み込み関数なのでこれはさすがに出題意図に沿っていないか...？

```py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
```

- 前提が`1 <= nums1.length, nums2.length <= 1000`なので、O(N^2)とかじゃない限りは計算量的にはどういうやり方でも問題にはならなさそう（可読性は別）
  - 仮にこれがもっと増えた時はちゃんと考える必要があるのでそういう解き方をしている人はいないだろうか

- https://github.com/mamo3gr/arai60/pull/13/files#diff-9168f775279a69eeec48cd74c26022e267c1b017acba90bde789d3fb412f2e73
- ソートを使うやり方もあるのか
```py
def intersectionWithoutSet(self, nums1: List[int], nums2: List[int]) -> List[int]:
    sorted1 = sorted(nums1)
    sorted2 = sorted(nums2)

    i, j = 0, 0
    common_numbers = []
    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] < sorted2[j]:
            i += 1
            continue
        elif sorted1[i] > sorted2[j]:
            j += 1
            continue

        common = sorted1[i]
        assert common == sorted2[j]
        common_numbers.append(common)

        while i < len(sorted1) and sorted1[i] == common:
            i += 1

        while j < len(sorted2) and sorted2[j] == common:
            j += 1

    return common_numbers
```

- https://github.com/mamo3gr/arai60/pull/13/files
  - 参考になる

>>片方がとても大きくて、片方がとても小さいときには、大きい方を set にするのは大変じゃないでしょうか、特に大きいほう が sort 済みのときにはどうしますか。

>ソート済みのケースも考えてみるか。

>>長いほうがソートされている場合, 長い方のリストをイテレーションするより二分探索で見つけるほうが良い.

>なるほど。`nums1`が短い方として、`N1`個の数字それぞれについて、`log N2` で二分探索できる。

>>他、両方ソートされていてとても大きければ、マージソートの変形のように書くと思います.

```py
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        return self.intersection(nums2, nums1)

    lookup = set(nums1)
    common = []
    for n in nums2:
        if n in lookup:
            common.append(n)
            lookup.remove(n)

        if not lookup:
            break

    return common
```
