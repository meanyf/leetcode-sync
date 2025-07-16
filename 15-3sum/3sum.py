#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        idx = 0
        res = []
        s = set()
        while idx < len(nums) - 2:
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                val = nums[idx] + nums[l] + nums[r]
                if val == 0:
                    item = [nums[idx], nums[l], nums[r]]
                    key = (nums[idx], nums[l], nums[r])
                    if key not in s:
                        s.add(key)
                        res.append(item)
                if nums[l] == nums[r]:
                    break
                if val < 0:
                    l += 1
                else:
                    r -= 1
            idx += 1
        return res
# @lc code=end


