class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1

        prefix_sum = 0
        answer = 0

        for num in nums:
            prefix_sum += num
            answer += prefix_sum_to_count[prefix_sum - k]
            prefix_sum_to_count[prefix_sum] += 1

        return answer