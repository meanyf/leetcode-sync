#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if nums[mi] > nums[hi]:
                lo = mi + 1
            else:
                hi = mi
        # lo
        ans = lo
        hi = len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if nums[mi] == target:
                return mi
            elif target < nums[mi]:
                hi = mi - 1
            else:
                lo = mi + 1
        lo = 0
        hi = ans - 1     
        while lo <= hi:
            mi = (lo + hi) // 2
            if nums[mi] == target:
                return mi
            elif target < nums[mi]:
                hi = mi - 1
            else:
                lo = mi + 1
        return -1

        
# @lc code=end

