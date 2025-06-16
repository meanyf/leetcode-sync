#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        cnt_zeros = nums.count(0)
        
        while lo <= hi:
            mi = (lo + hi) // 2
            if nums[mi] < 0:
                lo = mi + 1
            else:
                hi = mi - 1
        return max(lo, len(nums) - cnt_zeros - lo)
# @lc code=end

