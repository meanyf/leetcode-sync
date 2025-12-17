class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        res = 0
        for r, ch in enumerate(s):   
            d[ch] = d.get(ch, 0) + 1 
            while d[ch] == 2:
                d[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
