class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        for r in range(len(seats)):
            res = r
            if seats[r] == 1:
                break
        l = r
        while r < len(seats):
            res = max((r - l) // 2, res)
            l = r
            r += 1
            while r < len(seats) and seats[r] != 1:
                r += 1
        res = max(res, abs(len(seats) - 1 - l))
        return res