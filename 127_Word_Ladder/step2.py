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
    