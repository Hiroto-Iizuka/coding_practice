## Step1

- スタックを使って解く
  - スタックはListやListNodeで実現できる
- start/endの組み合わせと順番が合っているかをチェックする必要がありそう
  - 組み合わせはdict使えばできそう
    - `{'(': ')', '[': ']', '{': '}'}`
  - 順番があっているかどうかのチェックはどうしようか
    - ここまでで詰まったので生成AIにヒントをもらった
    - スタックの性質は「後入先出（LIFO）」
    - 開きカッコが出てきた場合は？
      - Listに格納しておく
      - 格納時にペアとなる閉じ括弧をstackに保存する？
    - 閉じ括弧が出てきた場合は？
      - Listの最後の値とペアが成立するかをチェックする
    - 最後に`stack_list == 0`ならTrueだな
- ヒントをもらいながら実装していった
  - けど、`WAになる→条件を足して対応する`のループに入ったので回答をみた(Step1)
  - というかわざわざ`list(s)`しなくてもいいんか
```python
# これはACしない
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        brackets = list(s)
        stack_list = []

        if len(brackets) == 1:
            return False

        if brackets[0] not in pairs:
            return False

        for char in brackets:
            if char in pairs:
                stack_list.append(pairs[char])
                continue
            if stack_list and stack_list.pop() != char:
                return False
            else:
                stack_list.append(char)
                
        if len(stack_list) == 0:
            return True
        else:
            return False
```

- 疑問
  - 初見の問題を解く時、実務のように途中の値を出力したりしてデバッグするよりも頭の中で考えた方が望ましいのだろうか？
  - 今回、模範回答は生成AIに頼ってみたのだが、他人の回答を見るのと生成AIの模範解答+他人の回答を読むとだとどっちがいいんだろう？読む過程さえ飛ばさなければよい？
    - 生成AIってどうしても魚だけを得ている気がしていて少し気になった
    - タイムリーにnodchipさんがポストしてた笑
      - https://x.com/nodchip/status/2004803405097922837?s=61
      - あくまで練習なのだから生成AIは使わないでおこうかな（上達したいなら使わない）

## Step2

- 個人的にifネストが苦手なのでまとめた
  - ただ今回のケースだとまとめない方が読みやすいかもしれない

- 最後は`return not stack_list`という書き方もある
  - https://github.com/komdoroid/arai60/pull/12/files#r2630417643
- 他の人のコード
  - 割とifネストを許容している人が多い？