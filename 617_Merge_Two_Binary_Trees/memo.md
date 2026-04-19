## Step1

- 2つのBTがあり、マージさせるというもの
- 重なるnodeのvalueの和をマージ後のtreeのnodeのvalueとする

### BFS

- depthとそのdepth内で何番目かを一緒に持たせておき、後から足すのはどうか
  - そもそもdepthいらないか、rootから順番に番号振っていけばよさそう
  - bfsする関数を用意しておく
    - これが返すべき値
      - `[(node, index)...]`
        - こっちだと配列を二つ作る必要があるのでメモリに負荷がありそう
      - `{ index: [node1, node2] }`
        - こっちならO(N)で合計出せそうなイメージがある

```py
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        index_to_nodes = collections.defaultdict(list)

        index_to_nodes = self.bfs(root1, index_to_nodes)
        index_to_nodes = self.bfs(root2, index_to_nodes)
        
        merged_nodes = { index: TreeNode(sum(nodes)) for index, nodes in index_to_nodes.items() }

        for i in merged_nodes:
            left = 2 * i + 1
            right = 2 * i + 2

            if left in merged_nodes:
                merged_nodes[i].left = merged_nodes[left]
            if right in merged_nodes:
                merged_nodes[i].right = merged_nodes[right]

        if not merged_nodes:
            return None
        return merged_nodes[0]

    def bfs(self, root: Optional[TreeNode], dictionary: dict) -> dict:
        if root is None:
            return dictionary
        queue = deque([(root, 0)])

        while queue:
            node, index = queue.popleft()
            dictionary[index].append(node.val)

            if node.left:
                queue.append((node.left, 2 * index + 1))
            if node.right:
                queue.append((node.right, 2 * index + 2))

        return dictionary      
```

### DFS（再帰）

- コード量は大きく減った
- 再帰に慣れていないので、何をやっているかはわかりづらいかも
- 計算量
  - O(N) : 木の高さの高い方
- ここまでスッキリ書けるのか

```py
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)

        return node
```

## Step2

### BFS

- step1を生成AIに見せて改善してもらった
- この程度の改善であれば元のコードの方が読みやすい気がする。こういう書き方もあるんだなくらいに思っておく。
- 今回のケースだと、再帰で書くのが一番シンプルでよさそう。

```py
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        queue = deque([(root1, root2)])

        while queue:
            node1, node2 = queue.popleft()
            node1.val += node2.val

            if node1.left and node2.left:
                queue.append((node1.left, node2.left))
            elif node2.left:
                node1.left = node2.left

            if node1.right and node2.right:
                queue.append((node1.right, node2.rigth))
            elif node2.right:
                node1.right = node2.right

        return root1
```

### DFS(反復)

- 以前、DFSは再帰か反復と教わったので反復を生成AIに作ってもらった。
- 計算量
  - O(N) : 木の高さの高い方

```py
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1

        stack = [(root1, root2)]

        while stack:
            node1, node2 = stack.pop()

            if node1 is None or node2 is None:
                continue

            node1.val += node2.val

            if node1.left is None:
                node1.left = node2.left
            else:
                stack.append((node1.left, node2.left))

            if node1.right is None:
                node1.right = node2.right
            else:
                stack.append((node1.right, node2.right))

        return root1
```

### 他の人のコードを見る

- https://github.com/naoto-iwase/leetcode/pull/22/changes#diff-71b591f216a80cf7ef1191bcc4e28df72fa47886531875cc18826914b5870065R11-R12

自分は（やることを忘れちゃうので）BFS/DFSをコード量で判断しがちだが、本来は上記の様に手数・制約・計算量で判断すべき

- https://github.com/naoto-iwase/leetcode/blob/311055d0bd74faa21fd1ff0c02b67c092a76b56e/0617-merge-two-binary-trees/0617-merge-two-binary-trees.md?plain=1#L97

BFSで書いている。コード量 = 可読性ではないのを実感した。
ただ、変数宣言が多く実際のコーディングテストの場だと、私の場合はちゃんと書けなくなりそう。

- https://github.com/mamo3gr/arai60/pull/22/changes#diff-c0740821568865adba38299a441de034ceffe301d6f08b613e8a85cb778e4c92R10

コードではないけど、ここまで緻密にメモリ使用量を見積もれると良い。

- https://github.com/mamo3gr/arai60/pull/22/changes#diff-afb2b8f4b1110499c2e68e416b7a995382ee351184175c4785ae75461d4c23e6R10-R27

root1またはroot2を返す時、deepcopyをつかっているのは非破壊的にやるためみたい。

- https://github.com/mamo3gr/arai60/pull/22/changes#diff-afb2b8f4b1110499c2e68e416b7a995382ee351184175c4785ae75461d4c23e6R40-R62

stackパターン。
再帰の場合、スタックオーバーフローの可能性があるので、深い木の場合はスタックを使うのがよさそう。
