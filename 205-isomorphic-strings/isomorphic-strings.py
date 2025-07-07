class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res = []
        d = {}
        vals = set()
        for ch1, ch2 in zip(s, t):
            if ch1 in d:
                res.append(d[ch1])
            else:
                if ch2 in vals:
                    return False
                d[ch1] = ch2
                res.append(d[ch1])
                vals.add(ch2)

        return res == list(t)