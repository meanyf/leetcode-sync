class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        item1 = bin(start)[2:]
        item2 = bin(goal)[2:]
        cnt = 0
        for i in range(1, max(len(item1), len(item2)) + 1):
            a = item1[-i] if i <= len(item1) else '0'
            b = item2[-i] if i <= len(item2) else '0'
            if a != b:
                cnt += 1 
        return cnt
