#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        cur = 0
        for num in nums:
            cur = max(num, cur + num)
            best = max(cur, best)
        return best
        #     if cur >= len(nums):
        #         return 0
        #     if nums[i] < 0 and nums[cur] > nums[i]:
        #         return max(res, run(i + 1, i + 1, nums[i + 1]))
        #     res += nums[i]
        #     return max(res, run(i + 1, i + 1, res))

        # return run(0, 0, 0)


# @lc code=end
