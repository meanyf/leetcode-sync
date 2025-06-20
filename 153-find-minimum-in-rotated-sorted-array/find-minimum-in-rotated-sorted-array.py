#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return min(nums)
        lo = 0
        hi = len(nums) - 1
        prev = (0, nums[0])
        while lo <= hi:
            print(lo,)
            mi = (lo + hi) // 2
            left = nums[mi - 1] if mi > 0 else float('-inf')
            right = nums[mi + 1] if mi < len(nums) - 1 else float('inf')
            if nums[mi] <= right and nums[mi] <= left:
                print('true')
                return nums[mi]
            if nums[mi] >= prev[1]:
                lo = mi + 1
            else:
                hi = mi - 1
            prev = (mi, nums[mi])
        return nums[lo] if lo < len(nums) else nums[0]
# @lc code=end

