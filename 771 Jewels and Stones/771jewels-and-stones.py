class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        cnt = 0
        for j in jewels:
            d[j] = True
        for s in stones:
            cnt += 1 if s in d else 0
        return cnt

        