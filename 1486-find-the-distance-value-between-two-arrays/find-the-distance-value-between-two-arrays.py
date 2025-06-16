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
                        print('exac')
                        cnt += 1
                    break
                if arr2[mi] < item:
                    lo = mi + 1
                else:
                    hi = mi - 1
            else:
                ok = True
                if lo < len(arr2) and abs(arr2[lo] - item) <= d:
                    ok = False
                if lo > 0 and abs(arr2[lo - 1] - item) <= d:
                    ok = False
                if ok:
                    cnt += 1

        return cnt
        
# @lc code=end

