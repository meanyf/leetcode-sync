#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for item in arr1:
            print(cnt)
            lo = 0
            hi = len(arr2) - 1
            while lo <= hi:
                mi = (lo + hi) // 2
                if arr2[mi] == item:
                    if abs(item - arr2[mi] > d):
                        cnt += 1
                    break
                if arr2[mi] < item:
                    lo = mi + 1
                else:
                    hi = mi - 1
            else:
                if lo == 0:
                    if abs(arr2[lo] - item) > d:
                        cnt += 1
                elif lo == len(arr2):
                    if abs(arr2[lo - 1] - item) > d:
                        cnt += 1
                elif lo == len(arr2) - 1:
                    if abs(arr2[lo] - item) > d and abs(arr2[lo - 1] - item) > d:
                        cnt += 1      
                elif 0 < lo < len(arr2) - 1:
                    if abs(arr2[lo] - item) > d and abs(arr2[lo - 1] - item) > d and abs(arr2[lo + 1] - item) > d:
                        cnt += 1

        return cnt
        
# @lc code=end

