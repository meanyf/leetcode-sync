class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        res = 0
        for k in d:
            if d[k] == 1:
                res += k
        return res