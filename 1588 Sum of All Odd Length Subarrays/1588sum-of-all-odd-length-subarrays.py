class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        s = 0
        nums = arr
        prefix_arr = [0] * (len(nums)+ 1)
        for i in range(1, len(nums) + 1):
			prefix_arr[i] = prefix_arr[i - 1] + nums[i - 1] 

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if (j - i) % 2 == 0:
                    s += prefix_arr[j + 1] - prefix_arr[i]
        return s

