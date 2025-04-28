class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = p2 = 0
        n2 = len(s)
        while p1 < len(t) and p2 < n2:
            if s[p2] == t[p1]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        if p2 == n2:
            return True

        return False
            