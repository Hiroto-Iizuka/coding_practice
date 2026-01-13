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
