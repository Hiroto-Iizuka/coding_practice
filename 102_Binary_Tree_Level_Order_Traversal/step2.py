class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values_by_level = []
        if root is None:
            return values_by_level

        frontier = [root]

        while frontier:
          next_frontier = []
          values = []

          for node in frontier:
              values.append(node.val)

              if node.left is not None:
                  next_frontier.append(node.left)
              if node.right is not None:
                  next_frontier.append(node.right)
              
          values_by_level.append(values)
          frontier = next_frontier

        return values_by_level
    