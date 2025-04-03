class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pref = [1] * (n + 1)
        suf = [1] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] * nums[i - 1]
        nums.reverse()
        for i in range(1, n + 1):
            suf[i] = suf[i - 1] * nums[i - 1]
        ans = [0] * n
        for i in range(1, n + 1):
            ans[i - 1] = pref[i - 1] * suf[-i - 1]
        return ans
            
        