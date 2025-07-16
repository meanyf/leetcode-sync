# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        mn = float('inf')
        for idx in range(len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                val = nums[idx] + nums[l] + nums[r]
                if abs(target - val) < mn:
                    mn = abs(target - val)
                    res = val
                    if target == val: return target
                elif val < target:
                    prev = nums[l]
                    l += 1
                    while l < r and prev == nums[l]:
                        l += 1
                else:
                    r -= 1
        return res
# @lc code=end