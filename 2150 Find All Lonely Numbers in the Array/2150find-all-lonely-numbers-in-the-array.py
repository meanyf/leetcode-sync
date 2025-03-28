class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        d = {}
        res = []
        for i, num in enumerate(nums):
            d[num] = d.get(num, 0) + 1
        
        for k in d:
            if d[k] == 1 and not (k + 1 in d or k - 1 in d):
                res.append(k)
        return res
