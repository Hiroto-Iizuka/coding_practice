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
