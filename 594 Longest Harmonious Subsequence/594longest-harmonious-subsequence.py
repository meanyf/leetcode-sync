class Solution:
    def findLHS(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        res = 0
        for num in d:
            if num - 1 in d:
                res = max(res, d[num] + d[num - 1])
        return res