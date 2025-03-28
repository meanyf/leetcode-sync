class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        
        cnt = 0
        for item in t:
            if item in s and d[item] > 0:
                d[item] -= 1
            else:
                cnt += 1
        return cnt