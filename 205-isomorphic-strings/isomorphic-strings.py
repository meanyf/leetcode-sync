class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res = []
        d = {}
        vals = set()
        for ch1, ch2 in zip(s, t):
            if ch1 in d:
                if d[ch1] != ch2:
                    return False
            else:
                if ch2 in vals:
                    return False
                d[ch1] = ch2
                vals.add(ch2)
        return True