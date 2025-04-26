class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        if n == 2:
            return s if s[0] == s[1] else s[0]

        max_len = 0
        start_idx = 0

        for center in range(n):
            max_rad = min(center, n - 1 - center)
            k = 0
            while k <= max_rad:
                if s[center - k] != s[center + k]:
                    break
                k += 1
            cur_len = 2 * (k - 1) + 1
            if cur_len > max_len:
                max_len = cur_len
                start_idx = center - (k - 1)
            if max_len == n:
                break

            max_rad = min(center, n - center)
            k = 0
            while k <= max_rad:
                if k > 0 and s[center - k] != s[center + k - 1]:
                    break
                k += 1
            cur_len = 2 * (k - 1)
            if cur_len > max_len:
                max_len = cur_len
                start_idx = center - (k - 1)
            if max_len == n:
                break

        return s[start_idx:start_idx + max_len]
