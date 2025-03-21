class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return i, d[target - num]
            d[num] = i


            