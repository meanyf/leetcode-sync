#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        prev = nums[0]
        while lo <= hi:
            mi = (lo + hi) // 2
            left = nums[mi - 1] if mi > 0 else float('-inf')
            right = nums[mi + 1] if mi < len(nums) - 1 else float('inf')
            if nums[mi] <= right and nums[mi] <= left:
                return nums[mi]
            if nums[mi] >= prev:
                lo = mi + 1
            else:
                hi = mi - 1
            prev = nums[mi]
        return nums[lo] if lo < len(nums) else nums[0]
# @lc code=end

