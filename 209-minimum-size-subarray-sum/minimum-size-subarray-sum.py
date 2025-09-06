class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        mn = float('inf')
        res = 0
        for r in range(len(nums)):
            res += nums[r]
            while res >= target:
                mn = min(mn, r - l + 1)
                res -= nums[l]
                l += 1
        return mn if mn < float('inf') else 0