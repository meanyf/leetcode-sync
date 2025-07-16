#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                val = nums[idx] + nums[l] + nums[r]
                if val == 0:
                    res.append([nums[idx], nums[l], nums[r]])
                    prev = nums[l]
                    l += 1
                    while l < r and prev == nums[l]:
                        l += 1
                elif val < 0:
                    l += 1
                else:
                    r -= 1
        return res
# @lc code=end

