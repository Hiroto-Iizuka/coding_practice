class Solution:
    def firstUniqChar(self, s: str) -> int:
        word_to_index = defaultdict(int)

        for i, word in enumerate(s):
            if word in word_to_index:
                word_to_index[word] = -1
                continue

            word_to_index[word] = i

        for index in word_to_index.values():
            if index != -1:
                return index

        return -1
