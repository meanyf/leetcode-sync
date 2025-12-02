class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        left = right = None
        while lo <= hi:
            mi = (lo + hi) // 2
            if target == nums[mi]:
                lo = mi + 1
                right = mi
            if target < nums[mi]:
                hi = mi - 1
            elif target > nums[mi]:
                lo = mi + 1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (lo + hi) // 2
            if target == nums[mi]:
                hi = mi - 1
                left = mi
            if target < nums[mi]:
                hi = mi - 1
            elif target > nums[mi]:
                lo = mi + 1
        return [left if left is not None else -1, right if right is not None else -1]