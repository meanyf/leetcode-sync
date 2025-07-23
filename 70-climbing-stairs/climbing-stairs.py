from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def run(n):
            if n == 0: return 1
            if n < 0: return 0
            return run(n - 2) + run(n - 1)
        
        return run(n)