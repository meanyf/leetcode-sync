class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rgb(left, r):
            return lstl[r] - lstl[left]
        lstl = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            lstl[i] = lstl[i - 1] + nums[i - 1]
        s = 0
        for i in range(len(nums)):
            s += rgb(max(0, i - nums[i]), i + 1)
        return s