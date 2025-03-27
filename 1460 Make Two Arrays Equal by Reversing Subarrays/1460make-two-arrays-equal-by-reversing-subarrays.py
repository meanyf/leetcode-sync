class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        d1 = {}
        d2 = {}
        for num in target:
            d1[num] = d1.get(num, 0) + 1 
        for num in arr:
            d2[num] = d2.get(num, 0) + 1 
        
        for k in d1:
            if not (k in d2 and d1[k] == d2[k]):
                return False 
        for k in d2:
            if not (k in d1 and d1[k] == d2[k]):
                return False 
        return True