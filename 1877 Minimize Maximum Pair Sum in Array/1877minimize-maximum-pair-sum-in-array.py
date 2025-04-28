class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        mn = 0
        l = 0
        n = len(nums)
        r = n - 1
        while l < r:
            mn = max(mn, nums[l] + nums[r])
            l += 1
            r -= 1
        return mn