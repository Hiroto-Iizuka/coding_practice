## Step1

- 最初に思いついたのは前から順番に取り出して、残りに同じ文字があるか検証するという解き方
- 計算量
  - 時間: O(N^2)
  - 空間: O(N)

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, ch in enumerate(s):
            if ch not in s[:i] + s[i+1:]:
                return i
        return -1
```

## Step2

- dictを使うのがよさそうなのはわかるが、実装までは思いつかず以下を見た
  - https://github.com/mamo3gr/arai60/pull/15/files#diff-1abed5bf15305d2097908dd35ec2a987156443dcb5b09f4325e26712e7bef596
- 時間計算量: O(N) 
- 空間計算量: O(k) ※文字列sの長さをn, 異なる文字数をk
