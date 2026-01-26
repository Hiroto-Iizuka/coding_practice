## Step1

- 配列の要素がintになっているなど細かな違いはあるが、200. Number of Islandsを少しいじれば実現できそう

### BFS

- 時間計算量: O(m * n)
- 空間計算量: O(min(m, n))

```py
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    current_area = self.bfs(grid, r, c)
                    max_area = max(max_area, current_area)

        return max_area

    def bfs(self, grid, r, c):
        frontier = deque()
        frontier.append((r, c))
        visited = grid
        area = 1
        visited[r][c] = 0

        while frontier:
            row, col = frontier.popleft()

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for d_row, d_col in directions:
                n_row, n_col = row + d_row, col + d_col

                if 0 <= n_row < len(visited) and 0 <= n_col < len(visited[0]) and visited[n_row][n_col] == 1:
                    frontier.append((n_row, n_col))
                    area += 1
                    visited[n_row][n_col] = 0

        return area
```

### DFS

- 再帰はどうも値を想像しづらい...
- 時間計算量: O(m * n)
- 空間: O(m * n) : 再帰スタックdfsをm * n回呼び出す

```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    current_area = self.dfs(grid, r, c)
                    max_area = max(max_area, current_area)

        return max_area

    def dfs(self, grid, r, c):
        visited = grid
        if not 0 <= r < len(visited) or not 0 <= c < len(visited[0]):
            return 0 

        if visited[r][c] == 0:
            return 0

        visited[r][c] = 0

        area = 1
        area += self.dfs(visited, r + 1, c)
        area += self.dfs(visited, r - 1, c)
        area += self.dfs(visited, r, c + 1)
        area += self.dfs(visited, r, c - 1)

        return area
```

## Step2

- bfs/dfsという関数名はやめておいた方が良さそう
  - Breadth-First Searchの名前だけど、島を探索しているイメージなのでexploreかな

### BFS

```py
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    current_area = self.explore_island(grid, r, c)
                    max_area = max(max_area, current_area)

        return max_area

    def explore_island(self, grid, r, c):
        frontier = deque()
        frontier.append((r, c))
        visited = grid
        area = 1
        visited[r][c] = 0

        while frontier:
            row, col = frontier.popleft()

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for d_row, d_col in directions:
                n_row, n_col = row + d_row, col + d_col

                if 0 <= n_row < len(visited) and 0 <= n_col < len(visited[0]) and visited[n_row][n_col] == 1:
                    frontier.append((n_row, n_col))
                    area += 1
                    visited[n_row][n_col] = 0

        return area
```

### DFS

```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    current_area = self.explore_island(grid, r, c)
                    max_area = max(max_area, current_area)

        return max_area

    def explore_island(self, grid, r, c):
        visited = grid
        if not 0 <= r < len(visited) or not 0 <= c < len(visited[0]):
            return 0 

        if visited[r][c] == 0:
            return 0

        visited[r][c] = 0

        area = 1
        area += self.explore_island(visited, r + 1, c)
        area += self.explore_island(visited, r - 1, c)
        area += self.explore_island(visited, r, c + 1)
        area += self.explore_island(visited, r, c - 1)

        return area
```

## Step3

### BFS

- `visited = grid`は参照をコピーしているだけだったので、新しく同じ形のgridを作ることで対応するようだ

```py
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    area = self.explore_island(grid, visited, r, c)
                    max_area = max(max_area, area)

        return max_area

    def explore_island(self, grid, visited, r, c):
        frontier = deque()
        frontier.append((r, c))
        area = 1
        visited[r][c] = True

        while frontier:
            row, col = frontier.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for d_row, d_col in directions:
                n_row, n_col = row + d_row, col + d_col

                if (0 <= n_row < len(grid) and 
                    0 <= n_col < len(grid[0]) and 
                    grid[n_row][n_col] == 1 and 
                    not visited[n_row][n_col]):
                    frontier.append((n_row, n_col))
                    area += 1
                    visited[n_row][n_col] = True

        return area
```

### DFS

```py
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    area = self.explore_island(grid, visited, r, c)
                    max_area = max(max_area, area)
        
        return max_area

    def explore_island(self, grid, visited, r, c):
        if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
            return 0
        
        if grid[r][c] == 0 or visited[r][c]:
            return 0
        
        visited[r][c] = True
        
        area = 1
        area += self.explore_island(grid, visited, r + 1, c)
        area += self.explore_island(grid, visited, r - 1, c)
        area += self.explore_island(grid, visited, r, c + 1)
        area += self.explore_island(grid, visited, r, c - 1)
        
        return area
```