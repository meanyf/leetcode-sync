class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        res = []
        while any(d.values()):
            lc = []
            for k in d:
                if d[k] > 0:
                    lc.append(k)
                    d[k] -= 1
            if lc:
                res.append(lc)
                
        return res
        