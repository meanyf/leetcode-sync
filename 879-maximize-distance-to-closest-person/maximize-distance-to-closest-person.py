class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = 0
        while l < len(seats) and seats[l] == 0:
            l += 1
        res = r = l
        while r < len(seats):
            if seats[r] == 1:
                res = max(res, (r - l) // 2)
                l = r
            r += 1
        res = max(res, abs(len(seats) - 1 - l))
        return res