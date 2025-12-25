## Step1

- 2つのListNodeの同じポインタどうしを足し合わせてあらたなListNodeを作るという問題
- 各nodeのvalは一桁、足して10以上になった場合は次のnode.valの和に+1として計算するため保持しておく必要がある
  - `if l1.val + l2.val > 10` のときに変数 1 or 0 を定義する
  - 一の位を取得する方法: `% 10`
  - 十の位を取得する方法: `// 10`
    - でも10の位が2以上になることはなさそうなので、+1の固定値でよさそう


```python3
# 1ループの処理
sum_num = l1_node.val + l2_node.val + carry_up_one
if sum_num > 10:
    carry_up_one = 1
    result_node.val = sum_num % 10
else:
    carry_up_one = 0
    result_node.val = sum_num % 10
result_node = result_node.next
l1_node = l1_node.next
l2_node = l2_node.next
```

- l1, l2の長い方のnextがNoneになるまでループ？
  - Memory Limit Exceededなのでここでギブアップ

```python3
result_node = ListNode()
l1_node = l1
l2_node = l2
carry_up_one = 0

while l1_node and l1_node.next:
    sum_num = l1_node.val + l2_node.val + carry_up_one
    if sum_num > 10:
        carry_up_one = 1
        result_node.val = sum_num % 10
    else:
        carry_up_one = 0
        result_node.val = sum_num % 10
    result_node.next = result_node
    l1_node = l1_node.next
    l2_node = l2_node.next

return result_node.next
```

## Step2

- Step1での考えた方は割と間違ってはなさそう
  - 
- ListNode関連を5問解いてきたわけだが、初見で同様の問題が出たときに回答できるかは正直不安
