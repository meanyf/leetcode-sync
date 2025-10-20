from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            cnt = 0
            for item in piles:
                cnt += ceil(item / speed)
                if cnt > h: return False
            return cnt <= h

        lo, hi = 1, max(piles)
        ans = None
        while lo <= hi:
            mi = (lo + hi) // 2
            if feasible(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans