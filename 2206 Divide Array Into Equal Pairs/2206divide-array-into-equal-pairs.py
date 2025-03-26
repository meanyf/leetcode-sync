class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for k in d:
            if d[k] % 2 != 0:
                return False
        return True
        