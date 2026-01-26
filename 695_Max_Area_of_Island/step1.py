from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        largest_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    current_area = self.bfs(grid, r, c)
                    largest_area = max(largest_area, current_area)

        return largest_area

    def bfs(self, grid, r, c):
        queue_to_visit = deque()
        queue_to_visit.append((r, c))
        visited = grid
        area = 1
        visited[r][c] = 0

        while queue_to_visit:
            row, col = queue_to_visit.popleft()

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for d_row, d_col in directions:
                n_row, n_col = row + d_row, col + d_col

                if 0 <= n_row < len(visited) and 0 <= n_col < len(visited[0]) and visited[n_row][n_col] == 1:
                    queue_to_visit.append((n_row, n_col))
                    area += 1
                    visited[n_row][n_col] = 0

        return area
