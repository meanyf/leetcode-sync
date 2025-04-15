class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        n = len(s)
        l = 0
        r = n - 1
        while l <= r:
            while l <= r and (ord(s[l]) < 65 or (ord(s[l]) > 90 and ord(s[l]) < 97) or ord(s[l]) > 122):
                l += 1
            while l <= r and (ord(s[r]) < 65 or (ord(s[r]) > 90 and ord(s[r]) < 97) or ord(s[r]) > 122):
                r -= 1
            if l <= r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)