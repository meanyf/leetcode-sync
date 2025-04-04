class Solution:
    def corpFlightBookings(self, bookings: list[list[int]], n: int) -> list[int]:
        dif = [0] * (n + 2)
        for l, r, x in bookings:
            dif[l] += x
            if r + 1 < (n + 1):
                dif[r + 1] -= x

        for i in range(1, n + 1):
            dif[i] += dif[i - 1]

        return dif[1:n+1] 