class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt = 0
        res = 0
        l = 0
        for r, item in enumerate(nums):
            cnt += 1 if item == 0 else 0
            while cnt > k:
                cnt -= 1 if nums[l] == 0 else 0
                l += 1
            res = max(res, r - l + 1)
        return res