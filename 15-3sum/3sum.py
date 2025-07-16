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
        prev = []
        print(nums)
        s = set()
        while idx < len(nums) - 2:
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                if nums[idx] + nums[l] + nums[r] == 0:
                    if [nums[idx], nums[l], nums[r]] != prev and ''.join(map(str, [nums[idx], nums[l], nums[r]])) not in s:
                        s.add(''.join(map(str, [nums[idx], nums[l], nums[r]])))
                        res.append([nums[idx], nums[l], nums[r]])
                    prev = [nums[idx], nums[l], nums[r]]
                # if nums[l] == nums[r]:
                #     break
                if nums[idx] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            idx += 1
        return res
# @lc code=end

