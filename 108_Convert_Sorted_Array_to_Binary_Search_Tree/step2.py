class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        root = TreeNode()

        node_with_start_to_end_indexes = [(root, 0, len(nums) - 1)]

        while node_with_start_to_end_indexes:
            node, start_index, end_index = node_with_start_to_end_indexes.pop()

            middle_index = (start_index + end_index) // 2
            node.val = nums[middle_index]

            if start_index < middle_index:
                node.left = TreeNode()
                node_with_start_to_end_indexes.append((node.left, start_index, middle_index - 1))

            if middle_index + 1 <= end_index:
                node.right = TreeNode()
                node_with_start_to_end_indexes.append((node.right, middle_index + 1, end_index))

        return root
    