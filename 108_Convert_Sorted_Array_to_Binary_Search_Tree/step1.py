class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        median_index = len(nums) // 2
        root = TreeNode(nums[median_index])

        queue = deque([(root, nums[:median_index], nums[median_index + 1:])])

        while queue:
            node, left_nums, right_nums = queue.popleft()

            if len(left_nums) != 0:
                left_median_index = len(left_nums) // 2
                node.left = TreeNode(left_nums[left_median_index])
                queue.append((node.left, left_nums[:left_median_index], left_nums[left_median_index + 1:]))

            if len(right_nums) != 0:
                right_median_index = len(right_nums) // 2
                node.right = TreeNode(right_nums[right_median_index])
                queue.append((node.right, right_nums[:right_median_index], right_nums[right_median_index + 1:]))

        return root
        