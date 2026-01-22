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

## Step3

- LRUのコメントを追ってて見つけたコード
  - https://discord.com/channels/1084280443945353267/1195700948786491403/1231538588529852426
  - 重複したものを`duplicated`に入れる
  - `unique_char_to_location`で重複していれば、duplicatedに入れる
  - 最後は`tuple(char, index)`の`[1]=index`を返している

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicated = set()
        unique_char_to_location = {}
        for i, c in enumerate(s):
            if c in duplicated:
                continue
            if c in unique_char_to_location:
                duplicated.add(c)
                del unique_char_to_location[c]
                continue
            unique_char_to_location[c] = i
        if not unique_char_to_location:
            return -1
        return next(iter(unique_char_to_location.items()))[1]
```