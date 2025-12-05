class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        cnt = 0
        for r in range(len(nums)):
            while l < len(nums) and nums[l] == 0:
                cnt += 1
                l += 1
            if l < len(nums):
               nums[r] = nums[l]
               l += 1
        
        for i in range(1, cnt + 1):
            nums[-i] = 0
        