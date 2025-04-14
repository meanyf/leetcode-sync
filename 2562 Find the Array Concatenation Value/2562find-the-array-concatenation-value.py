class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        val = 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            val += int(str(nums[l]) + str(nums[r])) if l != r else nums[l]
            l += 1
            r -= 1
        return val