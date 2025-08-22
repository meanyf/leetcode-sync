from functools import cache
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid = obstacleGrid
        m = len(grid)
        n = len(grid[0])
        @cache
        def run(x, y):
            if x >= m or y >= n:
                return 0
            if grid[x][y] == 1:
                return 0
            if x == m - 1 and y == n - 1:
                return 1

            return run(x + 1, y) + run(x, y + 1)
        return run(0, 0)