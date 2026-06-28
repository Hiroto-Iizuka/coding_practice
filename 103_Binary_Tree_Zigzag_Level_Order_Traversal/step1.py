class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values_by_level = []
        if root is None:
            return values_by_level

        node_with_level = deque([(root, 0)])

        while node_with_level:
            node, level = node_with_level.popleft()

            while len(values_by_level) <= level:
                values_by_level.append([])
            values_by_level[level].append(node.val)
            
            if node.left:
                node_with_level.append((node.left, level + 1))
            if node.right:
                node_with_level.append((node.right, level + 1))

        for level, values in enumerate(values_by_level):
            if level % 2 != 0:
                values.reverse()
        return values_by_level