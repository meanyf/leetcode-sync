#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            right = nums[mi + 1] if mi + 1 < len(nums) else float('-inf')
            left = nums[mi - 1] if mi - 1 > -1 else float('-inf')
            if left <= nums[mi] >= right:
                return mi
            if nums[mi] < right:
                lo = mi + 1
            else:
                hi = mi -1
        return -1

# @lc code=end

