class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        ans = 0
        for num in range(len(seats)):
            ans += abs(seats[num] - students[num])
        return ans