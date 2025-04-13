class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        res = [0] * len(s)
        ids = [i for i in range(len(s)) if s[i] == c]
        i1 = i2 = ids[0]
        if len(ids) > 1:
            i2 = ids[1]
    
        idx = 2
        print(ids)
        for i in range(len(s)):
            if s[i] == c and i == i2:
                i1 = i2
                i2 = ids[idx] if idx < len(ids) else 10**10
                idx += 1
                print(i1, i2)

            res[i] = min(abs(i - i1), abs(i - i2))
        return res