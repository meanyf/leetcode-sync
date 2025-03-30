class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        nums = sorted(nums, key=lambda x: x[0])
        left = nums[0][0]
        right = nums[0][1]
        cnt = right - left + 1
        for num in nums[1:]:
            if left <= num[0] <= right:
                if num[1] > right:
                    cnt += num[1] - right 
                    right = num[1]
            else:
                cnt += num[1] - num[0] + 1
                left = num[0]
                right = num[1]
        return cnt