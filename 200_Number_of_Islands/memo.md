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
