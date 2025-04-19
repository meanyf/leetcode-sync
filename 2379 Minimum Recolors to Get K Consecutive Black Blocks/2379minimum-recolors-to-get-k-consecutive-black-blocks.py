#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        cnt = 0
        for i in range(k):
            if blocks[i] == 'W':
                cnt += 1
        res = cnt
        l = 1
        r = k 
        while r < n:
            if blocks[l - 1] == 'W':
                cnt -= 1
            if blocks[r] == 'W':
                cnt += 1
            r += 1
            l += 1
            res = min(cnt, res)
        return res
            