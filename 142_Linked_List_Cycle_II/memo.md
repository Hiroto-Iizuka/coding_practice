## 142. Linked List Cycle II

## Step 1

- 141. Linked List Cycleとの差分は返り値のみと認識
- dictを使って `{ index: ListNode }`の形式で保持できると解決可能かなと考えたので以下の実装
    - でもこれだと`Runtime Error`となる

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        cur = head
        index = 0

        while cur:
            if cur.val in visited.values():
                return visited[cur.val]
            visited[index] = cur.val
            index += 1
            cur = cur.next

        return None
```

- ここで5分経っているので解答をみる
  - 完全に先入観だったことに気づく
  - set()の理解不足？
  - 問い自体は前問と全く変わっておらず、返り値が変わっていた
  - DescriptionのOutput例がわかりづらかったというのもある（回答の返り値の型ヒントをよくみる）

## Step 2

### コードを整える

- https://github.com/Hiroto-Iizuka/coding_practice/pull/1/files と変わらず

### 他の人のコード、コメントも見てみる

- `cur` を `node`, `current_node` と書く人もいた
- `visited` は `seen` とかでもいいのか、今回の問題だと好みかな

## Step 3
