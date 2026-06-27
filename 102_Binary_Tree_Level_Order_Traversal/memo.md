https://leetcode.com/problems/binary-tree-level-order-traversal/

## Step1

- BynaryTreeを階層ごとにリストにまとめる

### BFS

- 25分くらい
- `if len(values_by_level) == level:` を思いつくことができず生成AIに聞いた
  - 配列の要素番号と階層の一致を保証させることがわからなかった
- 計算量
  - 時間: O(N)
  - 空間: O(N)

```py
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
```

### DFS

- `if node.right:`と`if node.left`を逆に書いてたのでPassしなかった
- stackはLIFOなので順序が逆になるのか


```py
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

        return values_by_level
```

## Step2
### 他の人のコードを読む

- https://github.com/dorxyxki/arai60/pull/26/changes#diff-280e87756855c660d702d084567874fb558ce230e95b812c33d198de0c692113R39-R61

階層を管理せずに、同じ階層のものをまとめて `values` に入れていく方式
思えばBFS/DFSをパターン暗記（`queue・popleft()/stack・pop()`の組み合わせ）で覚えてしまっている気がする。
自分で書くなら以下の感じかな。階層を数値で管理する必要がなくシンプルになるのでよさそう。

```py
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
```

