class Solution:
    def minimumLength(self, s: str) -> int:
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        
        cnt = 0
        for k in d:
            cnt += 2 if d[k] > 1 and d[k] % 2 == 0 else 1
        return cnt