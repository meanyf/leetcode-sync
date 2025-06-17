#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i

        # nums.sort()
        # nums.append(len(nums))
        # for i, num in enumerate(nums):
        #     if i != num:
        #         return i
# @lc code=end

