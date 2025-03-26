class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        n = d[s[0]]
        for k in d:
            if n != d[k]:
                return False
        return True
