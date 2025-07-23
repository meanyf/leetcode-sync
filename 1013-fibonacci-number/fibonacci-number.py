from functools import cache 

class Solution:
    def fib(self, n: int) -> int:
        @cache
        def run(n):
            if n <= 1: return n
            return run(n - 1) + run(n - 2)
        
        return run(n)