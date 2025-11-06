class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = R = L = 0
        for item in s:
            R += 1 if item == 'R' else 0
            L += 1 if item == 'L' else 0
            res += 1 if R == L else 0
        return res