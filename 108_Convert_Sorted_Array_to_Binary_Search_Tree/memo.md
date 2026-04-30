## Step1

- 昇順になっている配列を、a height-balanced binary search treeに変換する問題

>A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

- BSTの条件：左サブツリーの全ノード < そのノード < 右サブツリーの全ノード
- 今回の付加条件：左右の高さ差が1以下
  - 中央値: 
    - [statistics.median()](https://docs.python.org/3/library/statistics.html#statistics.median)
    - https://github.com/python/cpython/blob/22c8590e40a13070d75b1e7f9af01252b1b2e9ce/Lib/statistics.py#L328
      - `median()`だとデータ数が偶数だと中央二つの平均を取ってしまうので、 [median_low](https://docs.python.org/3/library/statistics.html#statistics.median_low)または[median_high](https://docs.python.org/3/library/statistics.html#statistics.median_high)を使う
    - median系は値を返してしまうので、今回のケースだと、 `len (nums) // 2` で対応する
- やること
  - （今回はソート済み）
  - 受け取ったnumsの中央値を取り、それをrootとする
  - root（node）のindex - 1 の値を使ってleftのnodeをつくる、次のindex - 1の要素があればappendする
  - root（node）のindex + 1 の値を使ってrightのnodeをつくる、次のindex + 1の要素があればappendする

### BFS

- 上に書いたやることの手順では動かなかった
- 中央値を見つける→中央値で区切って2つの配列に分けるを繰り返す方法でできた
- 計算量（時間・空間）: スライスによってコピーが作られるのを考えると O(N log N)？
    - https://github.com/Yuto729/LeetCode_arai60/pull/29/changes#r2919540444

```py
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        median_index = len(nums) // 2
        root = TreeNode(nums[median_index])

        node_with_subarrays = deque([(root, nums[:median_index], nums[median_index + 1:])])

        while node_with_subarrays:
            node, left_nums, right_nums = node_with_subarrays.popleft()

            if len(left_nums) != 0:
                left_median_index = len(left_nums) // 2
                node.left = TreeNode(left_nums[left_median_index])
                node_with_subarrays.append((node.left, left_nums[:left_median_index], left_nums[left_median_index + 1:]))

            if len(right_nums) != 0:
                right_median_index = len(right_nums) // 2
                node.right = TreeNode(right_nums[right_median_index])
                node_with_subarrays.append((node.right, right_nums[:right_median_index], right_nums[right_median_index + 1:]))

        return root
```

### DFS(再帰)

- コード量は一番少ない
- Pythonの再帰制限やデバッグ難度から積極的に使いたくはない

```py
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) < 0:
            return None
        
        median_index = len(nums) // 2
        root = TreeNode(nums[median_index])
        root.left = self.sortedArrayToBST(nums[:median_index])
        root.right = self.sortedArrayToBST(nums[median_index + 1:])
        
        return root
```

### DFS（反復）

- ほぼBFSと同じ。stackになっただけ。

```py
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        median_index = len(nums) // 2
        root = TreeNode(nums[median_index])

        node_with_subarrays = [(root, nums[:median_index], nums[median_index + 1:])]

        while node_with_subarrays:
            node, left_nums, right_nums = node_with_subarrays.pop()

            if len(left_nums) != 0:
                left_median_index = len(left_nums) // 2
                node.left = TreeNode(left_nums[left_median_index])
                node_with_subarrays.append((node.left, left_nums[:left_median_index], left_nums[left_median_index + 1:]))

            if len(right_nums) != 0:
                right_median_index = len(right_nums) // 2
                node.right = TreeNode(right_nums[right_median_index])
                node_with_subarrays.append((node.right, right_nums[:right_median_index], right_nums[right_median_index + 1:]))

        return root
```

## Step2

### 他の人のコード

- https://github.com/mamo3gr/arai60/pull/23/changes#diff-0a4560c3f8a093598965b7471fc2a3b22f668b0fb2c6d3a9fdd2
- https://github.com/mamo3gr/arai60/pull/23/changes#diff-42dcab21ce751f482876063d49d9471b46f554a50e46214e677efaaa81c461d7R31

部分配列のコピーではなく、元の配列の開始・終了インデックスを持たせるという案よさそう。



### 参考にコード改善

- 計算量がO(N)に改善される

```py
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        root = TreeNode()

        node_with_start_to_end_indexes = [(root, 0, len(nums) - 1)]

        while node_with_start_to_end_indexes:
            node, start_index, end_index = node_with_start_to_end_indexes.pop()

            middle_index = (start_index + end_index) // 2
            node.val = nums[middle_index]

            if start_index < middle_index:
                node.left = TreeNode()
                node_with_start_to_end_indexes.append((node.left, start_index, middle_index - 1))

            if middle_index + 1 <= end_index:
                node.right = TreeNode()
                node_with_start_to_end_indexes.append((node.right, middle_index + 1, end_index))

        return root
```
