#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for item in t:
            d[item] = d.get(item, 0) + 1
        window = {}
        ans = (float("inf"), 0, 0)
        l = 0
        formed = 0
        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in d:
                if window[ch] == d[ch]:
                    formed += 1

            while l < len(s) and formed == len(d):
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                if window.get(s[l], 0) == d.get(s[l], 0) and window.get(s[l], 0) != 0:
                    formed -= 1
                if s[l] in window:
                    window[s[l]] -= 1
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


# @lc code=end
