class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        res = 0
        for i in range(len(s) - k + 1):
            cur = s[i:k + i]
            if int(cur) != 0 and num % int(cur) == 0:
                res += 1
        return res