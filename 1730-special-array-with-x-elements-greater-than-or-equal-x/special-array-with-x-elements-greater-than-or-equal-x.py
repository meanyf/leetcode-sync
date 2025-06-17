#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(nums[len(nums) - 1] + 1):
            lo = 0
            hi = len(nums)
            while lo <= hi:
                mi = (lo + hi) // 2
                if nums[mi] < i:
                    lo = mi + 1
                else:
                    hi = mi - 1
            if i == len(nums) - lo:
                return i
        return -1
# @lc code=end

