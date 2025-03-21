class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        r = 1
        length = len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                r = max(i + 1, r)
                while r != length and nums[r] == 0:
                    r += 1
                if r < length:
                    nums[i], nums[r] = nums[r], nums[i]
        
