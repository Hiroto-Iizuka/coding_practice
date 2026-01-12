import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        smallest_pairs = []
        min_sum_candidates = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_sum_candidates, (nums1[i] + nums2[0], i, 0))

        while min_sum_candidates and len(smallest_pairs) < k:
            _, nums1_index, nums2_index = heapq.heappop(min_sum_candidates)
            smallest_pairs.append([nums1[nums1_index], nums2[nums2_index]])

            next_nums2_index = nums2_index + 1
            if next_nums2_index < len(nums2):
                heapq.heappush(
                    min_sum_candidates,
                    (nums1[nums1_index] + nums2[next_nums2_index], nums1_index, next_nums2_index)
                )

        return smallest_pairs