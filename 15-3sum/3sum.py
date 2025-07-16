#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        idx = 0
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
                if val < 0:
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                else:
                    r -= 1
                    while r > l and nums[r + 1] == nums[r]:
                        r -= 1
        return res
# @lc code=end


