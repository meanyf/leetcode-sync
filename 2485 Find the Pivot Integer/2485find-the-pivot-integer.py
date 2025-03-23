class Solution(object):
    def pivotInteger(self, n):
        def rgb(left, r):
            return lstl[r] - lstl[left]
        nums = [i for i in range(1, n + 1)]
        length = len(nums) + 1
        lstl = [0] * (length)
        for i in range(1, length):
            lstl[i] = lstl[i - 1] + nums[i - 1] 

        for i in range(1, length):
            if rgb(0, i) == rgb(i - 1, length - 1):
                return i
        return -1
        