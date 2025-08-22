from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m = len(grid)
        n = len(grid[0])
        @cache
        def run(x, y):
            if x == m - 1 and y == n - 1 and grid[x][y] == 0:
                return 1
            down = run(x + 1, y) if x + 1 < m and grid[x][y] == 0 and grid[x + 1][y] == 0 else 0
            up = run(x, y + 1) if y + 1 < n and  grid[x][y] == 0 and grid[x][y + 1] == 0 else 0
            return down + up
        return run(0, 0)