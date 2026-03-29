## Step1

- rootから一番浅い階層にあるleafの階層を求める
- DFS/BFSの練習に使ってみる

### BFS

- maximum depthを求める場合は最後まで探索すればできた
- minimumのときは、nodeのright, leftが両方ともnullになったときの階層が答えになるはず
- 返す値が、`The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.`なので階層（= `depth`）を1から始める
- rootがNoneのケースはエッジケースとしてケアしておく
  - depthを0から始めて、return時に+1するでも動くはず。 `return depth + 1`
    - その場合、条件式をまとめることが可能。`if node is None or node.left is None and node.right is None:`
    - そうしない理由は、返す時の`+1`の意図正しく伝わるか不安、読み手に考察させる可能性があるため。
- `if node is None or node.left is None and node.right is None:`について
  - 前問でいただいた[コメント](https://github.com/Hiroto-Iizuka/coding_practice/pull/21#discussion_r2767176274)を反映してこの形にした
  - Google Style Guide: https://google.github.io/styleguide/pyguide.html#2144-decision
    - LeetCodeでは[特殊メソッド](https://docs.python.org/3/reference/datamodel.html#special-methods)があらかじめ定義されているかあら実害はないけど、実務上の観点ではそれがありうるという理解
    - なので、判定は `is None` で習慣づけておく
- 計算量 ※ノードの数をNとする
  - 時間: O(N)
  - 空間: O(N)

```py
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
```

### DFS

- 前問で[コメント](https://github.com/Hiroto-Iizuka/coding_practice/pull/21#discussion_r2767206502)いただいた通り、再帰・反復パターンを書いてみた

#### 再帰

- recursionlimit(default 1000回)に引っかかるリスクがある
  - 前問で[コメント](https://github.com/Hiroto-Iizuka/coding_practice/pull/21#discussion_r2776454069)いただいた
- 計算量 ※ノードの数をNとする
  - 時間: O(N)
  - 空間: O(N)

```py
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    def dfs(self, node):
        if node is None:
            return 0

        left = self.minDepth(node.left)
        right = self.minDepth(node.right)

        if left == 0:
            return right + 1
        if right == 0:
            return left + 1

        return min(left, right) + 1
```

#### ループ

- `min_depth`の初期値としての`float('inf')`は、なにと比べても比較対象をminとしてみなすことができる
- DFSの再帰と比べるとrecursionlimitがないのでよさそう
- BFSと比べるとDFSは全探索する必要があるため劣る
- 計算量 ※ノードの数をNとする
  - 時間: O(N)
  - 空間: O(N)

```py
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        INIT_DEPTH = 1
        stack = [(root, INIT_DEPTH)]
        min_depth = float('inf')

        while stack:
            node, depth = stack.pop()

            if node.left is None and node.right is None:
                min_depth = min(min_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return min_depth
```

## Step2

### 他の人のコード

- https://github.com/mamo3gr/arai60/blob/c53c9139fc220527d77bba864137dade33b118c1/111_minimum-depth-of-binary-tree/step3.py
  - 自分のコードだと、葉かどうかの判定式をそのままif文にしていたが、関数化することで何をしているのか明確になるのでよさそう
  - https://github.com/naoto-iwase/leetcode/pull/21/changes#diff-be01c72426972d275c9b4f090910360bf64a6635b79e16bb053916c86c7bcd6cR14
    - > 関数化はオーバーヘッドの割に合わないので行わない。
    - とあるように、関数化によるデメリットもあるのか
    - 自分はコメント入れるくらいにしておいた

- https://github.com/plushn/SWE-Arai60/pull/22/changes
  - https://github.com/plushn/SWE-Arai60/pull/22/changes#r2599126066
  - そうそう、自分も最初 `if not root` みたいに書いていたけど、全部rootで書くのに違和感があったので今の形にした
- https://github.com/plushn/SWE-Arai60/pull/22/changes#r2597641912
  - このコメントも参考になる
