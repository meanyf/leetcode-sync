class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        cnt = 0
        while l < n and r > l:
            while r > l and nums[l] + nums[r] >= target:
                r -= 1
            cnt += r - l
            l += 1
        return cnt