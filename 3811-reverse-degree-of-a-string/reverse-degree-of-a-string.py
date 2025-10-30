class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i + 1) * (ord('z') - ord(item) + 1) for i, item in enumerate(s))