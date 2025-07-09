class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        item = nums[0]
        for i in range(1, len(nums)):
            item ^= nums[i]
        return item