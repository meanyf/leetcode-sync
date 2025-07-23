from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def run(n):
            if n == 0: return 1
            if n < 0: return 0
            return run(n - 2) + run(n - 1)
        
        # return run(n)

        
        dp = [0] * (n + 1)
        dp[0] = 1
        if n > 0: dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]