class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vows = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] in vows and s[r] in vows:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vows:
                r -= 1
            else:
                l += 1
        return ''.join(s)