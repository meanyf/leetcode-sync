class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = 0
        while l < len(seats):
            if seats[l] == 1:
                break
            l += 1
        res = 0
        res = max(res, abs(0 - l))
        r = l + 1
        while r < len(seats):
            if seats[r] == 1:
                break
            r += 1
        
        if r == len(seats):
            if abs(0 - l) > abs(len(seats) - 1 - l):
                return abs(0 - l)
            else:
                return abs(len(seats) - 1 - l)
        
        while r < len(seats):
            res = max((r - l) // 2, res)
            l = r
            r += 1
            while r < len(seats) and seats[r] != 1:
                r += 1
        res = max(res, abs(len(seats) - 1 - l))
        return res