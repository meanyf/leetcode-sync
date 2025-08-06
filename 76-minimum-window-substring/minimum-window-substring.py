#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for item in t:
            d[item] = d.get(item, 0) + 1
        window = defaultdict(int)
        ans = (float("inf"), 0, 0)
        l = 0
        formed = 0
        filtered = [(i, ch) for i, ch in enumerate(s) if ch in d]
        for r, ch in filtered:
            if ch in d:
                window[ch] += 1
                if window[ch] == d[ch]:
                    formed += 1

            while l < len(s) and formed == len(d):
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                if s[l] in d and window[s[l]] == d[s[l]]:
                    formed -= 1
                if s[l] in window:
                    window[s[l]] -= 1
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


# @lc code=end
