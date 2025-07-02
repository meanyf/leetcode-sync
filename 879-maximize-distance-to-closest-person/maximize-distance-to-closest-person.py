#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = r = 0
        mx = 0
        while r < len(seats):
            while r < len(seats) and seats[r] == 0:
                r += 1
            if r == len(seats):
                mx = max(mx, r - l - 1)
            if l == 0 and seats[0] == 0:
                mx = max(mx, r - l)
            mx = max(mx, (r - l) // 2)
            l = r
            r += 1
        return mx
        

# @lc code=end

