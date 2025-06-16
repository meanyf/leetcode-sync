#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [0, 0]
        def lower_bound(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                if nums[mi] < target:
                    lo = mi + 1
                else:
                    hi = mi - 1
            return lo
        def upper_bound(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                if nums[mi] <= target:
                    lo = mi + 1
                else:
                    hi = mi - 1
            return lo
        def exact_match(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                if nums[mi] == target:
                    return True
                elif nums[mi] < target:
                    lo = mi + 1
                else:
                    hi = mi - 1
            return False
        if exact_match(nums, target):
            res[0] = lower_bound(nums, target)
            res[1] = upper_bound(nums, target) - 1
            return res
        else:
            return [-1, -1]
        
        
# @lc code=end

