class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] > nums[0]:
                l = m
            else:
                r = m
        return min(nums[l], nums[r])