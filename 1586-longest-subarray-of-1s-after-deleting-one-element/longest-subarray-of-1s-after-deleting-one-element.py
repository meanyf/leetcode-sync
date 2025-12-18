class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = res = l = 0
        for r, item in enumerate(nums):
            cnt += 1 if item == 0 else 0
            while cnt > 1:
                cnt -= 1 if nums[l] == 0 else 0
                l += 1
            res = max(res, r - l)
        return res