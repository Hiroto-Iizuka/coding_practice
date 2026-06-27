class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values_by_level = []

        if root is None:
            return values_by_level

        # 変数名は元の関数名と統一することを優先した。（自分でつけるなら`node_with_depth`にすると思う）
        node_with_level = deque([(root, 0)])

        while node_with_level:
            node, level = node_with_level.popleft()

            if len(values_by_level) == level:
                values_by_level.append([])
            
            values_by_level[level].append(node.val)

            if node.left:
                node_with_level.append((node.left, level + 1))
            if node.right:
                node_with_level.append((node.right, level + 1))

        return values_by_level 
