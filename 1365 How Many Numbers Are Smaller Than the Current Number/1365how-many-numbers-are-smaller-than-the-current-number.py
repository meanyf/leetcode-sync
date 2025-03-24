class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        nums_copy = nums[:]
        nums.sort(reverse=True)
        length = len(nums)
        d = {}
        i = 0
        for num in nums:
            d[num] = length - i - 1
            i += 1
        
        return [d[x] for x in nums_copy]
        