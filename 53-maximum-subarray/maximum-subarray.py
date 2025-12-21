class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        best = -math.inf
        for item in nums:
            cur = max(item, cur + item)
            best = max(best, cur)
        return best