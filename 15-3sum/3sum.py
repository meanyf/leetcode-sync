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
        print(nums)
        idx = 0
        res = []
        while idx < len(nums) - 2:
            l = idx + 1
            r = len(nums) - 1
            prev = []
            while l < r:
                val = nums[idx] + nums[l] + nums[r]
                if val == 0:
                    item = [nums[idx], nums[l], nums[r]]
                    if prev != item:
                        res.append(item)
                if nums[l] == nums[r]:
                    break
                prev = [nums[idx], nums[l], nums[r]]
                if val < 0:
                    l += 1
                else:
                    r -= 1
            prev = nums[idx]
            idx += 1
            while idx < len(nums) - 2 and nums[idx] == prev:
                idx += 1
            print(idx, end=', ')
        return res
# @lc code=end


