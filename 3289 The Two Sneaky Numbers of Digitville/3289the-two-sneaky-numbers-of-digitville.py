class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        d = {}
        cnt = 0
        lst = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] > 1:
                cnt += 1
                lst.append(num)
        return lst
        
        