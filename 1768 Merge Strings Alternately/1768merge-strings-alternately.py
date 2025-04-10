class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        s = ''
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        while p1 < n1 and p2 < n2:
            s += word1[p1] if i % 2 == 0 else word2[p2]
            p1 += 1 if i % 2 == 0 else 0
            p2 += 1 if i % 2 == 1 else 0
            i += 1

        if p1 < n1:
            s += word1[p1:]
        if p2 < n2:
            s += word2[p2:]
        return s