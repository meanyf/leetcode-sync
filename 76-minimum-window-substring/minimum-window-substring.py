import math
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        window = defaultdict(int)
        for item in t:
            d[item] += 1
        cnt = l = 0
        res = math.inf
        best_l, best_r = 0, -1
        size = len(d)
        for r, ch in enumerate(s):
            window[ch] += 1
            if ch in d and window[ch] == d[ch]:
                cnt += 1
            while l < len(s) and cnt == size:
                if r - l + 1 < res:
                    best_l, best_r = l, r
                    res = r - l + 1
                if s[l] in d and window[s[l]] == d[s[l]]:
                    cnt -= 1
                window[s[l]] -= 1
                l += 1
        return s[best_l: best_r + 1]
            
