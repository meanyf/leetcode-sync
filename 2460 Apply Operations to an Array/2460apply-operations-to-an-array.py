class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        cnt = 0
        res = []
        for num in nums:
            if num == 0:
                cnt += 1
            else:
                res.append(num)
        return res + [0] * cnt