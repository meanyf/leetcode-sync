#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        inf = float('inf')

        @cache
        def run(idx, taken):
            if idx == n and taken: return -inf
            if idx == n: return 0
            if taken: return max(run(idx + 1, 1), prices[idx])
            return max(run(idx + 1, 0), -prices[idx] + run(idx + 1, 1))

        return run(0, 0)
        # if not prices:
        #     return 0
        # buy = prices[0]
        # sell = 0
        # mx = 0
        # for item in prices[1:]:
        #     sell = item - buy
        #     buy = min(buy, item)
        #     mx = max(sell, mx)
        # return mx
# @lc code=end

