class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        mid = inorder.index(root_val)
        left_size = mid

        root.left = self.buildTree(preorder[1:1 + left_size], inorder[:mid])
        root.right = self.buildTree(preorder[1 + left_size:], inorder[mid + 1:])

        return root
    