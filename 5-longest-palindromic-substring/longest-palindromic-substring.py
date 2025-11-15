class Solution:
    def longestPalindrome(self, s: str) -> str:
        mx = -math.inf
        best_l = -1
        best_r = -2
        def expand(a, b):
            res = 0
            l, r = a, b
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            return l + 1, r - 1
        
        for i in range(len(s)):
            cur_l, cur_r = expand(i, i)
            if mx < cur_r - cur_l + 1:
                mx = cur_r - cur_l + 1
                best_l, best_r = cur_l, cur_r
            cur_l, cur_r = expand(i, i + 1)
            if mx < cur_r - cur_l + 1:
                mx = cur_r - cur_l + 1
                best_l, best_r = cur_l, cur_r
        return s[best_l: best_r + 1]
