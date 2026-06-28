## Step1

- 102とほぼ同様だが、levelが奇数の場合に逆順で結果を構築していく必要がある
- 時間計算量：O(N)
  - Pythonのステップ処理速度: 約100万〜1000万ステップ/秒
  - Nの最大値: 最大2,000
  - 最も遅い場合: 2,000 / 1,000,000 = 0.000002 秒 （2μs）
  - 最も速い場合: 2,000 / 10,000,000 = 0.0000002 秒 （0.2μs）
- 空間計算量：O(N)

### BFS

- 前の問題と同様だったので5分程度でできた
- levelが奇数のときに`values_by_level[level]`の一番前に入れるようにする？
  - これは一番前に入れるというコストが高いので避けたい
- appendleftという手もある
- 奇数のlevelだけreverseする方が良さそう

```py
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
```

### DFS

```py
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values_by_level = []

        if root is None:
            return values_by_level

        node_with_level = [(root, 0)]

        while node_with_level:
            node, level = node_with_level.pop()

            if len(values_by_level) == level:
                values_by_level.append([])
            
            values_by_level[level].append(node.val)

            if node.right:
                node_with_level.append((node.right, level + 1))
            if node.left:
                node_with_level.append((node.left, level + 1))

        for level, values in enumerate(values_by_level):
            if level % 2 != 0:
                values.reverse()
        return values_by_level
```

## Step2
### 他の人のコードを見る

- 102に近い問題ということもあり、自分が思いついた内容のいずれかが多い印象
