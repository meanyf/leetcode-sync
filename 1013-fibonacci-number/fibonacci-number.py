from functools import cache 

class Solution:
    def fib(self, n: int) -> int:
        @cache
        def run(n):
            if n <= 1: return n
            return run(n - 1) + run(n - 2)
        
        dp = [0] * (n + 1)
        if n > 0: dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        # return run(n)