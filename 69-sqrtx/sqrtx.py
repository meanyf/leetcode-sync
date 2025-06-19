#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 1
        hi = x
        while lo <= hi:
            mi = (lo + hi) // 2
            if mi**2 < x:
                lo = mi + 1
            else:
                hi = mi - 1
        if lo**2 == x:
            return lo
        if lo**2 > x:
            return lo - 1
# @lc code=end

