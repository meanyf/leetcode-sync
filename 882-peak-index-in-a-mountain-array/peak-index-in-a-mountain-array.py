#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo = 0
        hi = len(arr) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            right = arr[mi + 1] if mi + 1 < len(arr) else float('inf')
            left = arr[mi - 1] if mi - 1 > -1 else float('-inf')
            if arr[mi] > left and arr[mi] > right:
                return mi
            if arr[mi] >= right  and arr[mi] <= left:
                hi = mi - 1
            elif arr[mi] >= left and arr[mi] <= right:
                lo = mi + 1
        return -1
                

# @lc code=end

