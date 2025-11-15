class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = ''
        def expand(a, b):
            nonlocal mx
            res = 0
            l, r = a, b
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            if len(mx) < r - l - 1:
                mx = s[l + 1: r]
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return mx
        # for i in range(len(s) - 1):
            # mx = max(mx, expand(i, i + 1))
