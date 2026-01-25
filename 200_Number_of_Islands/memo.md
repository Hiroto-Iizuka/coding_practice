## Step1

- 15分考えてもとっかかりが掴めなかったので生成AIに聞きながら解いた
- DFS/BFSを使うらしい
- DFS
  - gridの行数をm, 列数をnとする
  - 時間計算量: O(m * n)
  - 空間: O(m * n) : 再帰スタックdfsをm * n回呼び出す
  - コード量という観点ではこっちの方が好みだなあ

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)

        return count

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return

    if grid[i][j] == '0':
        return

    grid[i][j] = '0'

    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
```

- BFS
  - 時間計算量: O(m * n)
  - 空間計算量: O(min(m, n))
    - DFSより有利

```py
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(grid, i, j)
        
        return count

def bfs(grid, i, j):
    queue = deque()
    queue.append((i, j))
    grid[i][j] = '0'
    
    while queue:
        x, y = queue.popleft()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                queue.append((nx, ny))
                grid[nx][ny] = '0'
```

## Step2

- 他の人がどう解いたかみてみる
- https://github.com/mamo3gr/arai60/pull/16/files#diff-35cfb01c3a280c6d684fbe67559a10fab18239367cce2c8a09c8603ccf3929e5
  - 変数名が整理されていてわかりやすい。これをStep1のコードに取り入れてみる

## Step3

### 再帰/bfs

- dfsメソッドをclassの内部に入れた
- gridを扱う時、行: r, 列: cとするとわかりやすくなった
- dfs内で使う入力値gridを変えずにvisitedという変数で管理するようにした

```py
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    self.dfs(grid, r, c)

        return count

    def dfs(self, grid, r, c):
        visited = grid
        if not 0 <= r < len(visited) or not 0 <= c < len(visited[0]):
            return

        if visited[r][c] == '0':
            return

        visited[r][c] = '0'

        self.dfs(visited, r + 1, c)
        self.dfs(visited, r - 1, c)
        self.dfs(visited, r, c + 1)
        self.dfs(visited, r, c - 1)
```                
### bfs

```py
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    self.bfs(grid, r, c)
        
        return count

    def bfs(self, grid, r, c):
        queue_to_visit = deque()
        queue_to_visit.append((r, c))
        visited = grid
        visited[r][c] = '0'
        
        while queue_to_visit:
            row, col = queue_to_visit.popleft()
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for d_row, d_col in directions:
                n_row, n_col = row + d_row, col + d_col
                
                if 0 <= n_row < len(visited) and 0 <= n_col < len(visited[0]) and visited[n_row][n_col] == '1':
                    queue_to_visit.append((n_row, n_col))
                    visited[n_row][n_col] = '0'             
```