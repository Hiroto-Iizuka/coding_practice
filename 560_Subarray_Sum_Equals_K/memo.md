## Step1 & Step2

- Two Sumに似ているような気がする
- 部分配列：元の配列から連続した要素を取り出して作られるより小さい配列
- numsは昇順になっているのだろうか？
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
      - それでも少し理解が辛いが、少しこの問題がキツいので先に進める

```py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        cumsum_to_freq = defaultdict(int)
        cumsum_to_freq[0] = 1
        for num in nums:
            total += num
            if total - k in cumsum_to_freq:
                count += cumsum_to_freq[total - k]

            cumsum_to_freq[total] += 1

        return count
```
