from functools import cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def run(i, j):
            if i == n:
                return 0
            return triangle[i][j] + min(run(i + 1, j), run(i + 1, j+ 1)) 
        return run(0, 0)