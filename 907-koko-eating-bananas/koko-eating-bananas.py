class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            cnt = len(piles)
            for item in piles:
                if item > speed:
                    cnt += item // speed
                    if item % speed == 0:
                        cnt -= 1
            return cnt <= h

        lo, hi = 1, max(piles)
        ans = None
        while lo <= hi:
            print(lo, hi)
            mi = (lo + hi) // 2
            if feasible(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans