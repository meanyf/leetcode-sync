class Solution:
    def maxFreqSum(self, s: str) -> int:
        chs = set(['a', 'e', 'i', 'o', 'u'])
        d1 = dict()
        d2 = dict()
        for ch in s:
            if ch in chs:
                d1[ch] = d1.get(ch, 0) + 1
            else:
                d2[ch] = d2.get(ch, 0) + 1
        mx1 = max(d1.values()) if d1.values() else 0
        mx2 = max(d2.values()) if d2.values() else 0
        return mx1 + mx2