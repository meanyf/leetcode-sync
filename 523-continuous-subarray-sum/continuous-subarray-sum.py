#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1:
            return False
        d = defaultdict(int)
        d[0] = -1
        prefix = 0
        cnt_zer = 0
        for i, num in enumerate(nums):
            prefix += num
            if num == 0:
                cnt_zer += 1
            else:
                cnt_zer = 0
            if cnt_zer > 1:
                return True
            if prefix % k in d:
                if i - d[prefix % k] >= 2:
                    return True
            else:
                d[prefix % k] = i
        return False


# @lc code=end
