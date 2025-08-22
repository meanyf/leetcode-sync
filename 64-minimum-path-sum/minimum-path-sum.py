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
            item = grid[x][y]
            return item + min(run(x + 1, y), run(x, y + 1))

        return run(0, 0)