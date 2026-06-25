class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        node_and_prefix_sum = [[root, root.val]]

        while node_and_prefix_sum:
            node, prefix_sum = node_and_prefix_sum.pop()

            if self.is_leaf(node) and prefix_sum == targetSum:
                return True

            if node.left:
                node_and_prefix_sum.append([node.left, prefix_sum + node.left.val])

            if node.right:
                node_and_prefix_sum.append([node.right, prefix_sum + node.right.val])

        return False

    def is_leaf(self, node):
        return node.left is None and node.right is None
    