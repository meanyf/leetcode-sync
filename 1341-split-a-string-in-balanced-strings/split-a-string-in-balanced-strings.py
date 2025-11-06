class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = balance = 0
        for item in s:
            balance += 1 if item == 'R' else -1
            res += 1 if balance == 0 else 0
        return res