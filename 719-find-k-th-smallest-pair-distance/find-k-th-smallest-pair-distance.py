class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def feasible(x):
            cnt = 0
            l, r = 0, 1
            while l < len(nums) - 1:
                if r < len(nums) and nums[r] - nums[l] <= x:
                    r += 1
                else:
                    cnt += r - l - 1
                    l += 1
            return cnt  
        lo, hi = 0, nums[-1] - nums[0]
        ans = None
        while lo <= hi:
            mi = (lo + hi) // 2
            if feasible(mi) >= k:
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans 