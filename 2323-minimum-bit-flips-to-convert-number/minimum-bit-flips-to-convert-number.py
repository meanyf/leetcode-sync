class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        item1 = bin(start)[2:][::-1]
        item2 = bin(goal)[2:][::-1]
        cnt = 0
        i = 0
        for i in range(max(len(item1), len(item2))):
            a = item1[i] if i < len(item1) else '0'
            b = item2[i] if i < len(item2) else '0'
            if a != b:
                cnt +=1 
        return cnt
