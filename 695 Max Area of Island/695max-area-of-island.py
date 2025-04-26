class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(x, y):
            visited[x][y] = True
            acc = 1
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if not visited[nx][ny] and grid[nx][ny] == 1:
                        acc += dfs(nx, ny)
            return acc
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res