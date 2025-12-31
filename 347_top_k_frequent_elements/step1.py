class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq_dic = defaultdict(int)
        for num in nums:
            freq_dic[num] += 1
        
        freq_ranking = sorted(freq_dic.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(freq_ranking[i][0])
        return result