class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur = sum(nums[:k])
        m = cur
        for i in range(k, len(nums)):
            cur = cur - nums[i - k] + nums[i]
            m = max(m, cur)
        return m / k