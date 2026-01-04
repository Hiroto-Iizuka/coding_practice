## Step1

- 元のListNodeを順番にstackに入れる
- stackから順番に取り出す
  - sentinel.nextに繋げていく
  - 現在のnodeのループの時に、直前のnode.nextに入れる
    - つまり、`prev_node`と`reverse_node`を用意する
    - 以下のように書いたがこれだとACしない

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []

        while node and node.next:
            stack.append(node)
            node = node.next

        reverse_node = ListNode()
        prev_node = sentinel = ListNode(next=node)
        while stack:
            reverse_node = stack.pop()
            prev_node.next = reverse_node
            prev_node = reverse_node

        return sentinel.next
```

  - 生成AIにヒントをもらいつつ以下を完成した。気が付けなかったのは以下の2点
    - stackに積むときのループ条件（node.nextは不要だった）
    - 最後のnode.nextにNoneを入れる（ListNodeの切れ目）

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        stack = []

        while node:
            stack.append(node)
            node = node.next

        reverse_node = ListNode()
        prev_node = sentinel = ListNode(next=node)
        while stack:
            reverse_node = stack.pop()
            prev_node.next = reverse_node
            prev_node = reverse_node
            if not stack:
                reverse_node.next = None

        return sentinel.next
```

## Step2

- dummyという変数名は少し苦手。「LeetCodeのListNodeにおける回答時の先頭」という意味合いの変数があるといいけど、それがdummyやsentinelになっている？
- 元のリストをそのままいじるやり方（https://github.com/tNita/arai60/pull/8/files#diff-49578176608b9dec72599534392c9c400a7bca195ff86238149a1ebed4236114R54）
  - わかりやすいし、新たな配列作り必要がないのは好み
  - 一方でstackを使った方が順番を入れ替えているんだなというのがわかりやすい気もした

```Python3
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original_node = head
        # 前のループでの反転させたリストの先頭
        reverse_head = None
        while original_node is not None:
            reverse_head = ListNode(original_node.val, reverse_head)
            original_node = original_node.next
        return reverse_head
```
