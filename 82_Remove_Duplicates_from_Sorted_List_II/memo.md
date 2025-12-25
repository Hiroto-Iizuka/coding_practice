## Step1

- 単純に隣り合う数値を取り除くようにすると奇数のときに1つ余ってしまう
- すぐ思いつくのは、
  - チェック対象を1つ固定（ `target` ）
  - それと一致しなくなるまでwhileループ
  - 一致しなくなった時点で、`target`をvalに持つnodeを削除する
  - 次の`target`を決める
  - これがListNodeでできるのかはわからない

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        last_fixed_node = dummy
        node = head

        while node and node.next:
            if node.val == node.next.val:
                while node.next and node.val == node.next.val:
                    node = node.next
                last_fixed_node.next = node.next
            else:
                last_fixed_node = last_fixed_node.next
            node = node.next

        return dummy.next
```

## Step2

- いくつか解答を見たけど上記か類似するものが多かった
- whileの中でwhileするのは抵抗あるがしかたなさそう
- 変数名をかえた
  - `dummy`はなんのことかわからないので`sentinel`とした
  - `last_fixed_node`も文脈的に把握しづらい気がした

## Step3

- 3回連続で解答できるようになる過程で、prev_nodeという変数名がよくないことに気づいた
  - 生成AIにも聞いたが、「最後に保持されたnode」という意味で`last_kept`や挿入位置 `insertion_point`という案が出た
  - もっと明示的にしたい。「どこまで削除するか」という命名で `delete_point` がよいかもしれない
- 最終的な結果を作るための `node`、どこまで削除するかを管理する `delete_point` 