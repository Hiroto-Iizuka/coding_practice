import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = collections.defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1
        
        frequency_ranking = sorted(num_to_frequency, key=num_to_frequency.get, reverse=True)
        return frequency_ranking[:k]