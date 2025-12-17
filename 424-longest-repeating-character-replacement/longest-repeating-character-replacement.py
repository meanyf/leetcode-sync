class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st = {item for item in s}
        l = res = 0
        for key in st:
            cnt = 0
            l = 0
            for r, ch in enumerate(s):
                cnt += 1 if key != ch else 0
                while cnt > k:
                    cnt -= 1 if key != s[l] else 0
                    l += 1
                res = max(res, r - l + 1)
        return res


        