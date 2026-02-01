## Step1

- `hit`が与えられたら`hot`というように1letterを置き換えた文字が隣接扱いになる
- 隣接するかどうかを判定する方法は？
  - word自体がnodeにあたるのか？
  - 手作業でやるとしたらこんな感じ
    - wordListから一つずつ取り出し、beginWordと一字違いのwordを探す
    - 上で見つけたwordと一字違いのwordを探す（を繰り返す）
    - wordListに見つからない場合、endWordと一字違いかどうかを確認する
  - では一字違いってどう判定するか
    - word同士を1文字ずつ比較して差分が1以内であること
- 時間計算量: O(N^2 * L)  next_word * wordListLength * wordLength
- 空間計算量: O(N)

```py
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
           return 0

        next_word = deque([(beginWord, 1)])
        visited = {beginWord}

        while next_word:
            word, steps = next_word.popleft()

            if word == endWord:
                return steps

            for candidate_word in wordList:
                if candidate_word in visited:
                    continue

                diff_count = 0
                for i in range(len(word)):
                    if word[i] != candidate_word[i]:
                        diff_count += 1
                        if diff_count > 1:
                            break

                if diff_count == 1:
                    visited.add(candidate_word)
                    next_word.append((candidate_word, steps + 1))

        return 0
```

## Step2

- 上記だと遅すぎるので、高速化の手段をAIに聞いたら双方向DFSを提案された
- 計算量自体はO(N * L^2 * 26)だが、双方向から探索しているため速いみたい

```py
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_set = set(wordList)
        
        begin_set = {beginWord}
        end_set = {endWord}
        visited = set()
        steps = 1

        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            next_set = set()
            for word in begin_set:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + c + word[i+1:]
                        
                        if candidate in end_set:
                            return steps + 1
                        
                        if candidate in word_set and candidate not in visited:
                            visited.add(candidate)
                            next_set.add(candidate)
            
            begin_set = next_set
            steps += 1

        return 0
```