class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_s(nums, left_bias):
            lo, hi = 0, len(nums) - 1
            res = -1
            while lo <= hi:
                mi = (lo + hi) // 2
                if target < nums[mi]:
                    hi = mi - 1
                elif target > nums[mi]:
                    lo = mi + 1
                else:
                    res = mi
                    if left_bias:
                        hi = mi - 1
                    else:
                        lo = mi + 1
            return res
        return [bin_s(nums, True), bin_s(nums, False)]