from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def run(x, y):
            if x >= m or y >= n:
                return float('inf')
            if x == m - 1 and y == n - 1:
                return grid[x][y]
            return min(run(x + 1, y) + grid[x][y], run(x, y + 1) + grid[x][y])

        return run(0, 0)