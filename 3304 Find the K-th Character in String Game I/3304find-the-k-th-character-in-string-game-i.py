class Solution:
    def kthCharacter(self, k: int) -> str:
        s = 'a'

        def m(k, s):
            if len(s) >= k:
                return s[k - 1]
            res = ''
            for i in range(len(s)):
                res += chr((ord(s[i]) - 97 + 1) % 26 + 97)
            return m(k, s + res)
        
        return m(k, s)