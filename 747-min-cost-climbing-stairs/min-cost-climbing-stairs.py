#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def run(i):
            if i >= n: return 0
            return cost[i] + min(run(i + 1), run(i + 2))
        return min(run(0), run(1))
# @lc code=end

