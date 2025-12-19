class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for r in range(len(nums)):
            while l < len(nums) and nums[l] == nums[r]:
                l += 1
            if l < len(nums) and r + 1< len(nums):
                nums[r + 1] = nums[l]
            if l >= len(nums):
                break
        return r + 1