class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        prefix = [0] * (len(nums) + 1)
        n = len(prefix) - 1
        result = [0] * len(nums)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        for i in range(n):
            result[i] = nums[i] * i - prefix[i] + (prefix[n] - prefix[i] - nums[i] * (n - i))
        return result

