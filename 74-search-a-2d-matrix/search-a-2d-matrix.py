#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [item for row in matrix for item in row]
        print(nums)
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if target == nums[mi]:
                return True
            if target > nums[mi]:
                lo = mi + 1
            else:
                hi = mi - 1
        return False

# @lc code=end

