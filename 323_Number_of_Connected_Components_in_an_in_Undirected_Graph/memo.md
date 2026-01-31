## Step1

- 連結したノードが1つのグループとした時、いくつのグループがあるかを問われている
- 15分悩んでもわからなかったので生成AIの回答を見た

### DFS

- 時間計算量: O(V+E) ※ノード数 + エッジ数
- 空間計算量: O(V+E)
- dfsという名称や`countComponents`の中に`dfs`が定義されているのが気になる
- graphは隣接リストを作っている
  - `{0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3]}`
  - `node_to_neighbor`と名称がよさそう
- `dfs`では、`graph`を使って、Componentの始まりから終わりを調べている
  - `explore_component`という名称の方がわかりやすそう

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        count = 0
        
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
```

### Union-Find

- 時間計算量: O(V+E) ※ノードの数とエッジの数
- 空間計算量: O(V+E)
- こういう解き方があるんだなくらいで留めておく。
  - parentを使って、ノードのグループ管理をするイメージ

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                return True
            return False
        
        components = n
        for u, v in edges:
            if union(u, v):
                components -= 1
        
        return components
```

## Step2

### DFS

- セルフレビューで気になった箇所を修正した

```py
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_neighbor = {i: [] for i in range(n)}
        for u, v in edges:
            node_to_neighbor[u].append(v)
            node_to_neighbor[v].append(u)
        
        visited = set()
        count = 0
        
        for i in range(n):
            if i not in visited:
                self.explore_component(i, visited, node_to_neighbor)
                count += 1
        
        return count

    def explore_component(self, node, visited, node_to_neighbor):
        visited.add(node)
        for neighbor in node_to_neighbor[node]:
            if neighbor not in visited:
                self.explore_component(neighbor, visited, node_to_neighbor)
```
