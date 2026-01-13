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
        for word in strs:  # O(N)
            normalized = "".join(sorted(word))  # O(w log w)
            normalized_to_words[normalized].append(word)  # O(1)

        return list(normalized_to_words.values())
```

- 比較した時にヒストグラムの方が計算量的に有利なのでヒストグラムを採用

## Step3

- レビュー内容を反映した
- 変数名の決め方の学び

>ファーストチョイスとして省略しない形を使用し、予約語と被ったり流石に変数名が長すぎたら別の言い回しを考え、それでも思いつかなければ末尾に_を追加したり、省略形を使用するのが良いのかな

```py
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_words = collections.defaultdict(list)

        for word in strs:
            counter = [0] * 26

            for ch in word:
              counter[ord(ch) - ord('a')] += 1

            counter_to_words[tuple(counter)].append(word)

        return list(counter_to_words.values())
```

- sortとの比較で学びになる観点
- https://github.com/Hiroto-Iizuka/coding_practice/pull/12/files#r2659229866

>時間計算量は確かにO(nk) vs O(nk log k)でカウンターの方が有利ですが、カウンターの方は文字列にアルファベットの小文字しか来ないことを前提としており、文字種の拡張性に欠けます。

>また、kはnに比べたら小さく、sorted(str)もstr.join()もネイティブコードで動くので割と速いので実行時間で見たらおそらく大きな問題（差）にはならず、可読性や拡張性の観点からも私ならソートする方法を採用すると思います。

>なお重要なのはどちらを選ぶかよりも、こうした多角的な観点で比較検討できるかどうかだと思います。
