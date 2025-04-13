class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s = list(s)
        while l < r:
            if s[l] != s[r]:
                s[l] = s[r] = min(s[l], s[r])
            l += 1
            r -= 1
        return ''.join(s)