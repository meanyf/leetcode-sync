#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        cnt_zero = 0
        mx = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                cnt_zero += 1
            while cnt_zero > 1:
                if nums[l] == 0:
                    cnt_zero -= 1
                l += 1
            mx = max(mx, r - l)
        return mx
            
# @lc code=end

