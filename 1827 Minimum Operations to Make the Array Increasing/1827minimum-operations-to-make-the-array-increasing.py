class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx - 1]:
                res = nums[idx - 1] - nums[idx] + 1
                ans += res
                nums[idx] += res
        return ans