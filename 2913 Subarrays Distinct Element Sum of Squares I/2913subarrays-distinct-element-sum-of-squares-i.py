class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        res = 0
        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                res += len(set(nums[i:j + 1]))**2
        return res