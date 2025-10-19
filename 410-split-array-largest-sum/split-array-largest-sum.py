class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(x):
            cnt = 0
            j = 1
            for i, item in enumerate(nums):
                cnt += item
                if cnt > x:
                    cnt = item
                    j += 1
                    
            return cnt <= x and j <= k
        lo, hi = max(nums), sum(nums)
        ans = None
        while lo <= hi:
            mi = (lo + hi ) // 2
            if feasible(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans