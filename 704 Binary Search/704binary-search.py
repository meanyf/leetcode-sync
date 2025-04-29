class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mi = (hi + lo) // 2
            if nums[mi] == target:
                return mi
            elif nums[mi] < target:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1