class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l = 0
        r = 1
        while l < n:
            while r < n and nums[r] % 2 != 0:
                r += 2
            if nums[l] % 2 != 0 and nums[r] % 2 == 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 2
                r += 2
                continue
            
            if nums[l] % 2 == 0:
                l += 2
        return nums