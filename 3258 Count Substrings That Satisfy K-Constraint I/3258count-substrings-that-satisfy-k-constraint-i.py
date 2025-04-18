class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = r = 0
        n = len(s)
        ones = zeros = 0
        res = 0
        while l < n :

            while r < n and (ones + s[r].count('1') <= k or zeros + s[r].count('0') <= k):
                if s[r] == '1': ones += 1
                else: zeros += 1
                r += 1

            res += r - l 
            if s[l] == '1': ones = max(0, ones - 1)
            if s[l] == '0': zeros = max(0, zeros - 1)

            l += 1
        return res