class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) <= len(nums2):
            nums1, nums2 = nums2, nums1  # 小さい方をnums1にする

        return list(set(nums1).intersection(nums2))