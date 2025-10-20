class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(x):
            cur = 0
            cnt = 1
            for i, item in enumerate(nums):
                cur += item
                if cur > x:
                    cur = item
                    cnt += 1
            return cnt <= k
        lo, hi = max(nums), sum(nums)
        cur = None
        while lo <= hi:
            mi = (lo + hi ) // 2
            if feasible(mi):
                cur = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return cur