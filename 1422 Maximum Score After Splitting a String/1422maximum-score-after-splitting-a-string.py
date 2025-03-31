class Solution:
    def maxScore(self, s: str) -> int:
        m = 0
        cnt = 0
        prefix_arr = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            prefix_arr[i] = prefix_arr[i - 1] + int(s[i - 1])
        zeros_left = ones_right = 0
        for i in range(1, len(s)):
            zeros_left = i - prefix_arr[i]
            ones_right = prefix_arr[len(prefix_arr) - 1] - prefix_arr[i]
            m = max(m, zeros_left + ones_right)
        return m
