class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        r = n - 1
        foundWord = False
        cnt = 0
        while r > -1:
            if s[r].isalpha():
                foundWord = True
                cnt += 1
            elif foundWord is True:
                return cnt
            r -= 1
        return cnt
