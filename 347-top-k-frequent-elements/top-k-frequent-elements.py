#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for item in nums:
            d[item] = d.get(item, 0) + 1
        lst = list(d.items())
        lst.sort(key = lambda x: -x[1])
        return [x[0] for x in lst[:k]]
# @lc code=end

