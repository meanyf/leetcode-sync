class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_arr = [0] * (len(nums)+ 1)
        for i in range(1, len(nums) + 1):
			prefix_arr[i] = prefix_arr[i - 1] + nums[i - 1] 
        
        cnt = 0
        for i in range(1, len(prefix_arr) - 1):
            if (-2 * prefix_arr[i] + prefix_arr[len(prefix_arr) - 1]) % 2 == 0:
                cnt += 1
        return cnt