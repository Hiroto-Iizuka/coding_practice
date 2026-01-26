from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self.explore_island(grid, r, c)
                    max_area = max(max_area, area)

        return max_area

    def explore_island(self, grid, r, c):
        frontier = deque()
        frontier.append((r, c))
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
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
    