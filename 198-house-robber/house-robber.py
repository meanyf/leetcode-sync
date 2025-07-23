#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def run(i):
            if i >= len(nums): return 0
            return max(nums[i] + run(i + 2), run(i + 1))
        return run(0)
# @lc code=end

