class Solution:
    def firstUniqChar(self, s: str) -> int:
        word_to_index = dict()

        for i, char in enumerate(s):
            if char in word_to_index:
                word_to_index[char] = -1
                continue

            word_to_index[char] = i

        for index in word_to_index.values():
            if index != -1:
                return index

        return -1
