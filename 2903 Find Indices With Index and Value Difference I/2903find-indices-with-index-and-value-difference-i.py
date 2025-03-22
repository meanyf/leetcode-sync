class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        left = 0
        right = indexDifference
        while left < len(nums):
            while right < len(nums):
                if abs(nums[right] - nums[left]) >= valueDifference:
                    return [left, right]
                else:
                    right += 1
            left += 1
            right = left + indexDifference
        return [-1, -1]
        