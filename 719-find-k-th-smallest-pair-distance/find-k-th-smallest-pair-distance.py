class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        def feasible(x):
            cnt = 0
            l, r = 0, 1
            for r in range(1, len(nums)):
                while nums[r] - nums[l] > x:
                    l += 1
                cnt += r - l
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