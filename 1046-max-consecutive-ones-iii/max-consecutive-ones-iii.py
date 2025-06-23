class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt_zero = 0
        mx = 0
        l = r = 0 

        while r < len(nums):
            if nums[r] == 0:
                cnt_zero += 1
            while cnt_zero > k:
                if nums[l] == 0:
                    cnt_zero -= 1
                l += 1
            mx = max(mx, r - l + 1)
            r += 1
        return mx