## Step1

- 二分探索木（BST）であるかどうかを判定する
  - 左の子ノードの値 < 親ノードの値 < 右の子ノードの値
- 今のnodeの値と左子ノードの値、右子ノードの値をそれぞれ比較していく

### BFS

- 15分で答えに辿り着けず
- 時間計算量:O(N)
  - Pythonのステップ処理速度: 約100万〜1000万ステップ/秒
  - Nの最大値: 最大10,000
  - 最も遅い場合: 10,000 / 1,000,000 = 0.00001 秒 （10μs）
  - 最も速い場合: 10,000 / 10,000,000 = 0.000001 秒 （1μs）
- 空間計算量:O(N)

```py
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        node_with_range = deque([(root, -inf, inf)])

        while node_with_range:
            node, min_range, max_range = node_with_range.pop()

            if not (min_range < node.val < max_range):
                return False

            if node.left:
                node_with_range.append((node.left, min_range, node.val))

            if node.right:
                node_with_range.append((node.right, node.val, max_range))

        return True
```

### DFS

```py
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        node_with_range = [(root, -inf, inf)]

        while node_with_range:
            node, min_range, max_range = node_with_range.pop()

            if not (min_range < node.val < max_range):
                return False

            if node.left:
                node_with_range.append((node.left, min_range, node.val))

            if node.right:
                node_with_range.append((node.right, node.val, max_range))

        return True
```

## Step2

### 他の人のコードを見る

- https://github.com/skypenguins/coding-practice/pull/39/changes#diff-0c860cd754249868513e4f9054206317fa33d0f548fc3896ac2b3e11822fd852R62

再帰版。コード量は減るが、やっぱりデバッグのしづらさを感じてしまう。
