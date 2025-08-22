from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        bst = float('inf')
        @cache
        def run(x, y):
            if x == m - 1 and y == n - 1:
                return grid[x][y]
            if x < m and y < n:
                return min(run(x + 1, y) + grid[x][y], grid[x][y] + run(x, y + 1))
            return float('inf')

        return run(0, 0)