#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        last = 0
        cnt = 1
        while n > last:
            n -= cnt
            last = cnt
            cnt += 1
        return last
# @lc code=end

