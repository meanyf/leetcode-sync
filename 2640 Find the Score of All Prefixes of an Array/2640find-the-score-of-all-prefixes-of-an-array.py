class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        m = nums[0]
        length = len(nums)
        ans = [0] * (length)
        total = 0
        for i in range(length):
            m = max(m, nums[i])
            nums[i] = m + nums[i]
            total += nums[i]
            ans[i] = total
        return ans