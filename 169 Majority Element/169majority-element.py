class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = 0
        el = nums[0]
        for num in nums:
            if el == num:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    el = num
                    cnt = 0
        return el