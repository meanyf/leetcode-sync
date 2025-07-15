#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import OrderedDict, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = OrderedDict()
        d2 = {}
        mn = float('inf')
        res = ()
        for item in nums:
            d[item] = d.get(item, 0) + 1
                    
        print(res)
        lst = list(d.items())
        print(lst)
        lst.sort(key = lambda x: -x[1])
        return [x[0] for x in lst[:k]]
# @lc code=end

