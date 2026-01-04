class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for st in strs:
            counter = [0] * 26
            
            for c in st:
                counter[ord(c) - ord('a')] += 1

            dic[tuple(counter)].append(st)

        return list(dic.values())