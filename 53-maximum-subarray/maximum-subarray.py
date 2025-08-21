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
        def run(i, cur):
            nonlocal bst
            bst = max(bst, cur)
            if i == n: 
                return cur
            if cur + nums[i] >= nums[i]:
                return run(i + 1, cur + nums[i])
            return run(i + 1, nums[i])
        run(0, float('-inf'))
        return bst
# @lc code=end