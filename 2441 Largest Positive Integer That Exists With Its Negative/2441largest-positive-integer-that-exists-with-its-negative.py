class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        m = -1
        for num in nums:
            if -num in d and abs(m) <= abs(num):
                m = abs(num)
        return m