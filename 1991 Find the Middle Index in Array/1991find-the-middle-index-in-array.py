class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rgb(left, r):
            return lstl[r] - lstl[left]
        length = len(nums) + 1
        cnt = 0
        lstl = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            lstl[i] = lstl[i - 1] + nums[i - 1]
        for i in range(len(lstl) - 1):
            if rgb(0, i) == rgb(i + 1, length - 1):
                return i
        return -1
        