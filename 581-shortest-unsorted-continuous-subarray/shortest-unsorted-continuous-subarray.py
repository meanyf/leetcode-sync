#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mn = nums[0]
        l = r = 0
        for i, num in enumerate(nums[:-1]):
            mn = max(mn, num)
            if mn > nums[i + 1]:
                l = i + 1
        mx = nums[-1]
        for i in range(len(nums) - 1, 0, -1):
            mx = min(mx, nums[i])
            if mx < nums[i - 1]:
                # print(mx, nums[i - 1])
                r = i - 1
        if l - r + 1 == 1:
            return 0
        return l - r + 1
# @lc code=end

