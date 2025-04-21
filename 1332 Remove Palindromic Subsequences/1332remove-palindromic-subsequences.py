class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        else:
            return 1
        a = b = 0
        for ch in s:
            if ch == 'a':
                a = 1
            if ch == 'b':
                b = 1
            if a + b == 2:
                return 2
        return a + b