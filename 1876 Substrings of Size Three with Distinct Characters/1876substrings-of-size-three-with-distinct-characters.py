class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        r = 3
        cnt = 0
        for i, item in enumerate(s):
            if r > len(s):
                break
            if len(set(s[i:r])) == 3:
                cnt += 1
            r += 1
        return cnt

