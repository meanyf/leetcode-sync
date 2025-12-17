from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        d = defaultdict(int)
        window = defaultdict(int)
        for item in s1:
            d[item] += 1
        l = 0
        for r, ch in enumerate(s2):
            window[ch] += 1
            while l < len(s2) and window[ch] > d[ch]:
                window[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1):
                return True
        return False 