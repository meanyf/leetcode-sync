class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        print(d)
        
        lst = sorted(d.items(), key=lambda x: (x[1], -x[0]))
        res = []
        for item in lst:
            res.extend([item[0]] * item[1])
        return res