#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        res = 0
        for i, num in enumerate(nums):
            prefix += num
            if prefix - k in d:
                res += d[prefix - k]
            d[prefix] += 1
        return res

# @lc code=end

