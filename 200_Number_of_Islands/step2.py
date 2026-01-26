from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        LENGTH_ROW = len(grid)
        LENGTH_COLUMN = len(grid[0])
        
        for i in range(LENGTH_ROW):
            for j in range(LENGTH_COLUMN):
                if grid[i][j] == '1':
                    count += 1
                    bfs(grid, i, j)
        
        return count

def bfs(grid, i, j):
    to_visit_queue = deque()
    to_visit_queue.append((i, j))
    grid[i][j] = '0'
    
    while to_visit_queue:
        x, y = to_visit_queue.popleft()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                to_visit_queue.append((nx, ny))
                grid[nx][ny] = '0'
                