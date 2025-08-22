from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def run(x, y):
            if x >= m or y >= n:
                return 0
            if x == m - 1 and y == n - 1:
                return 1
            return run(x + 1, y) + run(x, y + 1)
        return run(0, 0)