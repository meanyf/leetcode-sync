#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            left = nums[mi - 1] if mi > 0 else float('-inf')
            right = nums[mi + 1] if mi < len(nums) - 1 else float('inf')
            if nums[mi] != left and nums[mi] != right:
                return nums[mi]
            if mi % 2 == 0:
                if left == nums[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1
            else:
                if left == nums[mi]:
                    lo = mi + 1
                else:
                    hi = mi - 1
        return nums[0]
# @lc code=end

