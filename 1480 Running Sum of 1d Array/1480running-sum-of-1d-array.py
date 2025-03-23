class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        lstl = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            lstl[i] = lstl[i - 1] + nums[i - 1]
        return lstl[1:]