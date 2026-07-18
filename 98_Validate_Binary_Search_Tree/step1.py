class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        node_with_range = deque([(root, -inf, inf)])

        while node_with_range:
            node, min_range, max_range = node_with_range.pop()

            if not (min_range < node.val < max_range):
                return False

            if node.left:
                node_with_range.append((node.left, min_range, node.val))

            if node.right:
                node_with_range.append((node.right, node.val, max_range))

        return True
