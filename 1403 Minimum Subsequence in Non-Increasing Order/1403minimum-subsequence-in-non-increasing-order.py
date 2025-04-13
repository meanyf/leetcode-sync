class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        l = 0
        r = len(nums) - 1
        summ1 = summ2 = 0
        res = []
        while l <= r:
            if summ1 <= summ2 + nums[r]:
                res.append(nums[l])
                summ1 += nums[l]
                l += 1
            else:
                summ2 += nums[r]
                r -= 1
        return res
