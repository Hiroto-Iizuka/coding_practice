## 141. Linked List Cycle

## Step 1

- Linked Listというデータ構造のことをよく知らない
  - 配列内の要素のことを「ノード」という
  - ノードには前後または両方のデータへの参照情報（リンク、ポインタ）を持っている
- `val`（値） と `next`(ポインタ)で構成される
- 双方向リストの場合、`prev`もある
- 解法の想像ができず答えを見た

## Step 2

### コードを整える

- 見た答えはだいぶ整っているようにみえる。
- curがcurrentの略称で若干伝わりづらい可能性もあるが、自身は文脈で予想できるためそこまで違和感を感じていない

### 他の人のコード、コメントも見てみる

- うさぎとかめというらしい。[こちら](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.2k4z0wt6ytf9)を見るにこの方法ではなく、setを使うことが大事みたい。

```
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
```

## Step 3

- current, curだと文脈的に把握しづらいとわかってきた（意味合いが広すぎるため）
- whileの条件: `while node:`だと`None, boolのfalse, 0, "", []`など意味合いが広く思わぬ挙動になる可能性がある
  - `while is not None:`とすることで条件が限定的・明確になる
