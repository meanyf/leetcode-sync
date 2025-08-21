#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
from functools import cache
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        bst = float('-inf')
        @cache
        def run(i):
            if i == n - 1: 
                return nums[-1]
            return max(nums[i], nums[i] + run(i + 1))
            
        for i in range(n):
            bst = max(bst, run(i))
        return bst
# @lc code=end
