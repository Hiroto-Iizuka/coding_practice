## Step1

- アナグラム問題は文字の登場回数が同一の文字列同士はアナグラムの関係である
- なのでアルファベット26字のカウンターリストをつくることが多い
  - ヒストグラムというらしい（[参考](https://github.com/mamo3gr/arai60/pull/12/files#diff-e8128c8fa57dd87ef72ff83460ca245b9c4013a76ffd12aa321979c5c81b5e2cR14)）
- 以前解いたときは以下の回答だった
  - 計算量
    - 時間: O(nk) n: strsの数、k: 各単語の文字数
    - 空間: O(nk) n: strsの数、k: 各単語の文字数
  - step2は可読性を意識して修正してみる

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for st in strs:
            counter = [0] * 26
            
            for c in st:
                counter[ord(c) - ord('a')] += 1

            dic[tuple(counter)].append(st)

        return list(dic.values())
```

## Step2

- カウンターやdictの名称をわかりやすく変更した
- [ここ](https://github.com/Hiroto-Iizuka/coding_practice/pull/10#discussion_r2658671322)で指摘いただいたように`import collections`と書く
- ソート版のコードのようにwordという名称もわかりやすいのでそうした

```py
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_word = collections.defaultdict(list)
        
        for word in strs:
            alphabet_counter = [0] * 26
            
            for ch in word:
                alphabet_counter[ord(ch) - ord('a')] += 1

            counter_to_word[tuple(alphabet_counter)].append(word)

        return list(counter_to_word.values())
```

- 参考: 単語ごとにsortする方法
  - 計算量
    - 時間 O(N * wlogw * 1)
    - 空間 O(nk) n: strsの数、k: 各単語の文字数

```py
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        normalized_to_words = collections.defaultdict(list)
        for word in strs: # O(N)
            normalized = "".join(sorted(word)) # O(w log w)
            normalized_to_words[normalized].append(word) # O(1)

        return list(normalized_to_words.values())
```

- 比較した時にヒストグラムの方が計算量的に有利なのでヒストグラムを採用