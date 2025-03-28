class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        res = []
        for word in words:
            if len(set(pattern)) != len(set(word)):
                continue
            d = {}
            lcw = True
            for i, s in enumerate(pattern):
                temp = d[s] if s in d else False
                d[s] = word[i]
                if temp and d[s] != temp:
                    lcw = False
                    break
            if lcw:
                res.append(word)
        return res
                