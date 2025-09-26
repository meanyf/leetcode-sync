#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from functools import cache
from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        @cache
        def run(n):
            if n == 0: return 0 # дошли до конца
            res = float('inf')
            for i in range(1, int(sqrt(n)) + 1):
                res = min(res, 1 + run(n - i*i))
            return res
        return run(n)
    
# @lc code=end