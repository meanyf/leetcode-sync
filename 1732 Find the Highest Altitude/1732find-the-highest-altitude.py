class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        lstl = [0] * (len(gain) + 1)
        m = 0
        for i in range(1, len(gain) + 1):
            lstl[i] = lstl[i - 1] + gain[i - 1]
            m = max(m, lstl[i])
        return m