#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
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
        nums.sort()
        lower = lower_bound(nums, target)
        upper = upper_bound(nums, target)
        return [x for x in range(lower, upper)]
# @lc code=end

