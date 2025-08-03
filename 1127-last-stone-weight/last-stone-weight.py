#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = stones[:]
        for i in range(len(res)):
            res[i] = -res[i]
        print(res)
        heapq.heapify(res)
        while len(res) > 1:
            item1 = heapq.heappop(res)
            item2 = heapq.heappop(res)
            if item1 != item2:
                heapq.heappush(res, item1 - item2)
        if not res:
            return 0
        return -res[0]

# @lc code=end
