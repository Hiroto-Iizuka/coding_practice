class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_index = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diff_to_index:
                return [diff_to_index[diff], i]
            else:
                diff_to_index[num] = i
