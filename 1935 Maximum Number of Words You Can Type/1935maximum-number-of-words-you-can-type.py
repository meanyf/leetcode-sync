class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        d = {}
        for s in brokenLetters:
            d[s] = True
        lst = text.split()
        cnt = 0
        for item in lst:
            for s in item:
                if s in d:
                    break
            else:
                cnt += 1
        return cnt