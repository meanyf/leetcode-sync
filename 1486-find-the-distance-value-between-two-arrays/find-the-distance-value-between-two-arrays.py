class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0

        for x in arr1:
            lo, hi = 0, len(arr2) - 1
            found = False

            while lo <= hi:
                mid = (lo + hi) // 2
                if abs(arr2[mid] - x) <= d:
                    found = True
                    break
                elif arr2[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid - 1

            if not found:
                cnt += 1

        return cnt
