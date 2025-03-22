class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        lstl = [0] * (len(nums))
        rstl = [0] * (len(nums))

        for i in range(1, len(nums)):
            lstl[i] = lstl[i - 1] + nums[i - 1]
        nums.reverse()

        for i in range(1, len(nums)):
            rstl[i] = rstl[i - 1] + nums[i - 1]
        
        rstl.reverse()
        return [abs(lstl[i] - rstl[i]) for i in range(len(rstl))]
        