class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        cumsum_to_freq = defaultdict(int)
        cumsum_to_freq[0] = 1
        for num in nums:
            total += num
            if total - k in cumsum_to_freq:
                count += cumsum_to_freq[total - k]

            cumsum_to_freq[total] += 1

        return count