class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for item in nums:
            res = min(res, sum(map(int, str(item))))
        return res