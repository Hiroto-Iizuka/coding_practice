## Step1

- ローカル
  - `+`以後は無視
  - `.`は無視
- ドメイン
  - 純粋なユニークをみる
- 手順
  - @より前: `.`, `+`以後を削除する
    - partition(), regexなどいろいろ使えるものはありそう
  - そのemailをkeyとしてdictでカウント
  - とりあえずただ書いた
    - 変数の再定義、変数名などは改善しないと
    - 計算量 4ms
      - 時間: emailsは`n`, emailの文字数`m`としたときに `O(nm)`
        - 参考: https://github.com/mamo3gr/arai60/pull/14/files#diff-3dfcbe543833ec5b353690dcd6cad6f62866717552428609199731a1f1c7e149R5
      - 空間: ``O(nm)`
        - dic: emailの長さ(n) * ユニーク数(m)
    - もっといい方法はあるか

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dic = defaultdict(int)

        for email in emails:
            email_tuple = email.partition("@")
            
            local_name = email_tuple[0]
            domain_name = email_tuple[2]

            if "+" in local_name:
                local_name = local_name.partition("+")[0]

            if "." in local_name:
                local_name = local_name.replace(".", "")

            email = local_name + "@" + domain_name
            dic[email] += 1

        return len(dic.keys())
```

- 変数名やdefaultdictの呼び出し元を追加した
- 一度定義した変数への再代入をやめたいがいい方法が思いつかない

```py
from collections import defaultdict

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = collections.defaultdict(int)

        for email in emails:
            local_name, _, domain_name = email.partition("@")

            local_name = local_name.partition("+")[0]
            local_name = local_name.replace(".", "")

            normalized = f"{local_name}@{domain_name}"
            unique_emails[normalized] += 1

        return len(unique_emails)
```

## Step2

- これ見やすい気がする
  - https://github.com/mamo3gr/arai60/pull/14/files#diff-83acbe1d6327f5560b1c9bd695a9986bb1cb8a1f45bb56cdfefd7ca2a3a3ad3b
  - `*rest` tuple/list のアンパックにおいて、この形式の変数は余った要素を配列として受け取るらしい
  - `@@`になっている場合などのエラーハンドリング

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local_name, domain_name, *rest = email.split("@")
            if rest:
                raise ValueError(f"There are two or more @ in {email}")

            local_name_normalized = local_name.replace(".", "").split("+")[0]
            unique_emails.add((local_name_normalized, domain_name))

        return len(unique_emails)
```

## Step3

- 実務上を考えると変数定義に型ヒントを入れて将来的なバグリスクを低減できるのは良いと思った
- つい一行でまとめたくなってしまうが、local_name_normalizedのように分割してわかりやすいことを心がけたい
- `splitmax=1`を入れてみた。`+`が複数ある場合を想定しているのだと思った。

```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails: set[tuple[str, str]] = set()

        for email in emails:
            split_result = email.split("@")
            if len(split_result) != 2:
                raise ValueError(f"email address '{email}' must contain only one @")
            local_name, domain_name = split_result

            local_name_deleted_dot = local_name.replace(".", "")
            local_name_normalized = local_name_deleted_dot.split("+", maxsplit=1)[0]
            unique_emails.add((local_name_normalized, domain_name))

        return len(unique_emails)
```
