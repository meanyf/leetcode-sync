class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        d = {}
        r = 0
        l = 0
        for ch in s:
            if ch in d and d[ch] == 2:
                break
            d[ch] = d.get(ch, 0) + 1
            r += 1
        ans = 0
        ans = max(ans, r - l)
        while r < n:
            if s[r] in d:
                if d[s[r]] == 2:
                    d[s[l]] -= 1
                    l += 1
                    continue
            d[s[r]] = d.get(s[r], 0) + 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
