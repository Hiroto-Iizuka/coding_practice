## Step1

巡回方法
- preorder: 行きがけ順
  - 根 -> 左 -> 右
- inorder: 通りがけ順
  - 左 -> 根 -> 右
- postorder（帰りがけ順）というのもあるらしい
  - https://zenn.dev/kueharx/articles/6e0362c9xc28a65#dfs(%E5%B8%B0%E3%82%8A%E3%81%8C%E3%81%91%E9%A0%86)
  - 左 -> 右 -> 今いる場所（根）
- 与えられる２つの巡回法から二分木を返すというもの
- 生成AIに聞きながら解答

### 再帰

- `preorder[0]` は根となる
- `inorder`を`preorder[0]`の値で分割すると、左・右で分けられる

```py
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
```

### 反復

```py
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        nodes = [root]
        inorder_index = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            parent = None

            while nodes and nodes[-1].val == inorder[inorder_index]:
                parent = nodes.pop()
                inorder_index += 1

            if parent:
                parent.right = node
            else:
                nodes[-1].left = node

            nodes.append(node)

        return root
```

## Step2

### 他の人のコードを読む

- https://github.com/Manato110/LeetCode-arai60/pull/29/changes#diff-869f8d49a392e4dfc7634bce97439d85f9e700f84632df88bbbf57504324c72bR143-R168

この問題に関して言えば反復は正直読みづらいな...と思っていたけど、うまく言語化できない。なんとなくこれは読みやすい気がするけどなんだろう

- https://github.com/rimokem/arai60/pull/29/changes#diff-3571f2f83b9aab1f837cac55ddc323917d5095c1a4d1844b0661d78f0d46718dR44

メモリの節約の観点
