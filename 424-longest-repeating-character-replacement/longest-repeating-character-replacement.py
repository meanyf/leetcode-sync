#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = set()
        mx = 0
        for ch in s:
            d.add(ch)

        for key in d:
            cnt = 0
            r = 0
            for l in range(len(s)):
                r = max(r, l)
                while r < len(s) and cnt <= k:
                    if s[r] != key:
                        cnt += 1
                    if cnt > k:
                        mx = max(mx, r - l)
                    else:
                        mx = max(mx, r - l + 1)
                    r += 1
                if s[l] != key:
                    cnt -= 1
        return mx
                

# @lc code=end

