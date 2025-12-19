class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        cnt = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            else:
                cnt += 1

        for i in range(1, cnt + 1):
            nums[-i] = 0