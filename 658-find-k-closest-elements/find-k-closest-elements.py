#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if arr[mi] < x:
                lo = mi + 1
            else:
                hi = mi
        print(lo)
        if lo == len(arr) or (lo == 0 and arr[lo] == x):
            if lo == 0:
                return sorted(arr[:k])
            if lo == len(arr):
                return sorted(arr[-k:])
        
        l = lo
        if arr[lo] != x:
            if abs(x - arr[lo - 1]) <= abs(x - arr[lo]):
                l = lo - 1
            else:
                l = lo
        r = l + 1
        cnt = 0
        res = []
        while cnt < k:
            left = arr[l] if l > -1 else float('inf')
            right = arr[r] if r < len(arr) else float('inf')
            if abs(x - left) <= abs(x - right):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            cnt += 1
        res.sort()
        return res
# @lc code=end

