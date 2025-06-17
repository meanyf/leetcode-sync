#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)
# @lc code=end

