## Step1

- 一番深い階層を出力する問題

### BFS

- キューを使って解ける
- 時間：O(N)
- 空間：O(N)

```py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        value_and_depth = deque([(root, 1)])
        max_depth = 0

        while value_and_depth:
            node, current_depth = value_and_depth.popleft()
            max_depth = max(max_depth, current_depth)

            if node.left:
                value_and_depth.append((node.left, current_depth + 1))
            if node.right:
                value_and_depth.append((node.right, current_depth + 1))

        return max_depth
```

### DFS

- 再帰
- 時間：O(N)
- 空間：O(H)
  - H = 木の高さ
- 単純な計算量だけだとこっちの方よさそう

```py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
```

- 生成AIにも聞いてみたが、stackを使ったやり方もあるみたい
- まあ、コード量の観点では再帰でいいかな

```py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [(root, 1)]
        max_depth = 0
        
        while stack:
            node, current_depth = stack.pop()
            max_depth = max(max_depth, current_depth)
            
            if node.right:
                stack.append((node.right, current_depth + 1))
            if node.left:
                stack.append((node.left, current_depth + 1))
        
        return max_depth
```

## Step2

- 他の人のコードを見たが、上記の3種類のいずれかを書いている印象
