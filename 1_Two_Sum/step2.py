class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_to_index:
                return [complement_to_index[complement], i]
            else:
                complement_to_index[num] = i
