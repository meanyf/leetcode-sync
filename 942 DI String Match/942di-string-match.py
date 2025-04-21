class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        d  = n
        i = 0
        res = [0] * (n + 1)
        for j in range(len(s)):
            if s[j] == 'I':
                res[j] = i
                i += 1
            else:
                res[j] = d
                d -= 1
        if s[n - 1] == 'I':
            res[n] = i
        else:
            res[n] = d
        return res