from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        INIT_DEPTH = 1
        que = deque([(root, INIT_DEPTH)])

        while que:
            node, depth = que.popleft()

            if node.left is None and node.right is None:
                return depth
            else:
                if node.left:
                    que.append((node.left, depth + 1))
                if node.right:
                    que.append((node.right, depth + 1))
        
        return depth
