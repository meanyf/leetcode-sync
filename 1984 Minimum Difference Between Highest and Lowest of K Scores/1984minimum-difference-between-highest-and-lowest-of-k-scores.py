class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        nums.sort()
        ans = float('inf')
        l = 0
        r = k - 1
        while r < n:
            ans = min(ans, abs(nums[l] - nums[r]))
            l += 1
            r += 1
        
        return ans