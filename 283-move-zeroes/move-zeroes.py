#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 1
        while l < len(nums) and r < len(nums):
            if nums[l] == 0:
                r = l + 1
                while r < len(nums) and nums[r] == 0:
                    r += 1
                if r < len(nums) and nums[r] != 0:
                    nums[l], nums[r] = nums[r], nums[l]
            
            else:
                l += 1
    
# @lc code=end

