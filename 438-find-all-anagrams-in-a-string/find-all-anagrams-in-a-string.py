from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = defaultdict(int)
        window = defaultdict(int)
        for item in p:
            d[item] += 1
        l = 0
        res = []
        for r, ch in enumerate(s):
            window[ch] += 1
            while window[ch] > d[ch]:
                window[s[l]] -= 1
                l += 1
            
            if r - l + 1 == len(p):
                res.append(l)
        return res