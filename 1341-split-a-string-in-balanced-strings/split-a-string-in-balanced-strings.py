class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = R = L = 0
        for item in s:
            if item == 'R':
                R += 1
            else:
                L += 1
            if R == L:
                res += 1
        return res