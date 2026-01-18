## Step1

- 15分考えてもとっかかりが掴めなかったので生成AIに聞きながら解いた
- DFS/BFSを使うらしい
- DFS
  - gridの行数をm, 列数をnとする
  - 時間計算量: O(m * n)
  - 空間: O(m * n) : 再帰スタックdfsをm * n回呼び出す
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
- コード量も少なく、かなり読みやすい

```py
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H, W = len(grid), len(grid[0])
        N = H*W
        visited = [False for _ in range(N)]
        ans = 0
        for i in range(N):
            if visited[i] or grid[i // W][i % W] == "0":
                continue

            ans += 1                
            que = deque([i])                
            while que:
                u = que.popleft()
                if visited[u]:
                    continue

                visited[u] = True
                uy, ux = u // W, u % W
                for j in range(4):
                    vy, vx = uy + dy[j], ux + dx[j]
                    v = vy * W + vx
                    if 0 <= vy and vy < H and 0 <= vx and vx < W and grid[vy][vx] == "1" and (not visited[v]):
                        que.append(v)

        return ans                        
```

- 自力で解けること自体がすごいなと思いました

```py
import collections


class Solution:
    WATER = "0"
    LAND = "1"

    def _is_land(self, grid: List[List[int]], i: int, j: int) -> bool:
        NUM_ROWS = len(grid)
        NUM_COLUMNS = len(grid[0])
        if i < 0 or i >= NUM_ROWS:
            return False
        if j < 0 or j >= NUM_COLUMNS:
            return False
        return grid[i][j] == self.LAND

    def _mark_connecting_lands_visited(
        self, grid: List[List[str]], visited: List[List[bool]], i: int, j: int
    ) -> List[List[bool]]:
        to_be_traversed = collections.deque()
        to_be_traversed.append((i, j))
        visited[i][j] = True
        while to_be_traversed:
            i, j = to_be_traversed.popleft()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor_i = i + di
                neighbor_j = j + dj
                if not self._is_land(grid, neighbor_i, neighbor_j):
                    continue
                if visited[neighbor_i][neighbor_j]:
                    continue
                to_be_traversed.append((neighbor_i, neighbor_j))
                visited[neighbor_i][neighbor_j] = True

        return visited

    def numIslands(self, grid: List[List[str]]) -> int:
        NUM_ROWS = len(grid)
        NUM_COLUMNS = len(grid[0])
        visited = [[False] * NUM_COLUMNS for _ in range(NUM_ROWS)]
        num_islands = 0
        for i in range(NUM_ROWS):
            for j in range(NUM_COLUMNS):
                if grid[i][j] == self.WATER:
                    continue

                assert grid[i][j] == self.LAND
                if visited[i][j]:
                    continue

                num_islands += 1
                visited = self._mark_connecting_lands_visited(grid, visited, i, j)

        return num_islands
```