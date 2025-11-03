class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        item = start ^ goal
        return bin(item)[2:].count('1')