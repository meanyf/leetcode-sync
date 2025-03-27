class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        d = {}
        for num in arr1:
            d[num] = d.get(num, 0) + 1
        res = []
        for num in arr2:
            res.extend([num] * d[num])
        ext = []
        
        d = {}
        for num in arr2:
            d[num] = True
        
        for num in arr1:
            if num not in d:
                ext.append(num)
        ext.sort()

        return res + ext