class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mx = -math.inf
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    mx = max(mx, nums[j] - nums[i])
        if mx > -math.inf:
            return mx
        return -1