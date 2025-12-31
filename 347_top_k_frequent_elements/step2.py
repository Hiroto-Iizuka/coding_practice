class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq_dic = defaultdict(int)
        for num in nums:
            freq_dic[num] += 1
        
        freq_ranking = sorted(freq_dic, key=freq_dic.get, reverse=True)
        return freq_ranking[:k]