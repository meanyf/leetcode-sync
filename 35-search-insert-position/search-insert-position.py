#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if nums[mi] == target:
                return mi
            if nums[mi] > target:
                hi = mi - 1
            else:
                lo = mi + 1
        if hi > lo:
            return lo - 1
        else:
            return hi + 1
# @lc code=end