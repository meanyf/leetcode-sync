class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(item if i % 2 == 0 else - item for i, item in enumerate(nums))