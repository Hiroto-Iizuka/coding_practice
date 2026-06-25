## step1

- rootからleafの合計値がtargetSumと一致するpathがあればtrueを返す
- パッと思いつくのはDFS

### stack

- 33分
- 時間計算量：O(N)
- 空間計算量：O(N)

```py
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        node_and_remaining = [[root, root.val]]

        while node_and_remaining:
            node, remaining = node_and_remaining.pop()

            if self.is_leaf(node) and remaining == targetSum:
                return True

            if node.left:
                node_and_remaining.append([node.left, remaining + node.left.val])

            if node.right:
                node_and_remaining.append([node.right, remaining + node.right.val])

        return False

    def is_leaf(self, node):
        return node.left is None and node.right is None
```

### recursive

```py
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        if root.left is None and root.right is None:
            return root.val == targetSum

        remaining = targetSum - root.val

        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
```

### BFS

```py
from collections import deque

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        queue = deque([[root, root.val]])

        while queue:
            node, remaining = queue.popleft()

            if self.is_leaf(node) and remaining == targetSum:
                return True

            if node.left:
                queue.append([node.left, remaining + node.left.val])

            if node.right:
                queue.append([node.right, remaining + node.right.val])

        return False

    def is_leaf(self, node):
        return node.left is None and node.right is None
```

## step2

### 他の人のコードを読む

- DFS/BFSのいずれかで解いている
- 2分で書いている人を見てすごいとなった

- https://github.com/SuperHotDogCat/coding-interview/pull/37/changes#diff-986655d2c103c00429d53bfc38091e6fb9d218c841caaa6e6b60463b20ab4146R6
  - 自分は累積和を使ったが、以下のようにtargetSumからそのまま引き算でやっている人もいた
> 引き算先にしちゃって、
> ...
> のほうが素直ではないでしょうか。
>https://discord.com/channels/1084280443945353267/1225849404037009609/1258455843226255361
  - 以下のように書ける

```py
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        node_and_remaining = [[root, targetSum - root.val]]

        while node_and_remaining:
            node, remaining = node_and_remaining.pop()

            if self.is_leaf(node) and remaining == 0:
                return True

            if node.left:
                node_and_remaining.append([node.left, remaining - node.left.val])

            if node.right:
                node_and_remaining.append([node.right, remaining - node.right.val])

        return False

    def is_leaf(self, node):
        return node.left is None and node.right is None 
```