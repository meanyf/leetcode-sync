#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo = 0
        hi = n 
        while lo <= hi:
            k = (lo + hi) // 2
            ans = k * (k + 1) // 2
            if ans <= n:
                lo = k + 1
            else:
                hi = k - 1
        return lo - 1
        
        # last = 0
        # cnt = 1
        # while n > last:
        #     n -= cnt
        #     last = cnt
        #     cnt += 1
        # return last
# @lc code=end

