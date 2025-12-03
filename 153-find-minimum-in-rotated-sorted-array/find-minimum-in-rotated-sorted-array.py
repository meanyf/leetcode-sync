class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return min(nums[1], nums[0])
        l, r = 0, len(nums) - 1
        x = y = 0
        res = math.inf
        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[l], nums[r], nums[m])
            if nums[m] > nums[0]:
                l = m + 1
                x += 1
            else:
                r = m - 1
                y += 1 
        return res