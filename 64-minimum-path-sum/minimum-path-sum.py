from functools import cache
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        @cache
        def run(x, y):
            if x == m - 1 and y == n - 1:
                return grid[x][y]
            down = run(x + 1, y) + grid[x][y] if x + 1 < m else float('inf')
            up = grid[x][y] + run(x, y + 1) if y + 1 < n else float('inf')
            return min(down, up)

        return run(0, 0)