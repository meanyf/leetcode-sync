class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ds = {}
        dt = {}

        for i in range(len(s)):
            ds[s[i]] = i
        for i in range(len(t)):
            dt[t[i]] = i

        res = 0
        for s in dt:
            res += abs(dt[s] - ds[s])
        return res