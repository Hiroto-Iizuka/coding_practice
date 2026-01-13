class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter_to_st = defaultdict(list)
        
        for st in strs:
            alphabet_counter = [0] * 26
            
            for c in st:
                alphabet_counter[ord(c) - ord('a')] += 1

            counter_to_st[tuple(alphabet_counter)].append(st)

        return list(counter_to_st.values())