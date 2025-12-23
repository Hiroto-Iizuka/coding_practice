## Step 1

- set()を使うだけ？
  - これでは通らない
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        unique_nums = set()
        cur = head

        while cur:
            if cur in unique_nums:
                continue
            unique_nums.add(cur)
            cur = cur.next

        return list(unique_nums)
```

通らない理由：
LeetCodeの問題の常識がよくわかってなかった。
`Output: [1, 2]` と書いてあるから `return list()`になるかと思ってた。
そうではなく、最後に正しいheadだけ返せば、内部でnextを辿って正解をチェックしてくれるのね。

- 5分で解けないので解答をみる
  - https://github.com/aki235/Arai60/pull/3/files#diff-9a053fdf9569fd0182ff71f7d62a42ad61915a4bcb35f3bd407d7f72e26ed1faR50
  - めちゃくちゃシンプル。意味も理解しやすい。

## Step 2

### コードを整える

- 一番シンプルだなと思ったやつを選んだので特に変更なし
- 今回から変数を `node` に変えた
  - 理由は重複削除のためにnodeを繋ぎ替える必要があったので、その処理だとわかりやすいようにListedNodeの名称から取った


### 他の人のコード、コメントも見てみる

- https://github.com/aki235/Arai60/pull/3/files#diff-9a053fdf9569fd0182ff71f7d62a42ad61915a4bcb35f3bd407d7f72e26ed1faR33

```Python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node:
            if prev and prev.val == node.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next

        return head
```

個人的には`prev`は「直前の」とか「一つ前の」という意味だと思ったので良いと思った。
しかし[こちらのコメント](https://github.com/aki235/Arai60/pull/3/files#r2608851457)にもあるように、別の意味で捉えられる可能性もあるのでもう少しピンポイントな名前の方がいいのかと思った。
その他の観点でも、PythonのListNodeは単方向リストを示しているように認識しているので、使わなくて済むならprevを実装する必要はないと思った。