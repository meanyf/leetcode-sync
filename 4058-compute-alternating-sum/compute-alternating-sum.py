class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        res = 0
        for i, item in enumerate(nums):
            res += item if i % 2 == 0 else - item
        return res