class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mn = nums[0]
        mx = -1
        for item in nums[1:]:
            mn = min(mn, item)
            if item > mn:
                mx = max(mx, item - mn)
        return mx

