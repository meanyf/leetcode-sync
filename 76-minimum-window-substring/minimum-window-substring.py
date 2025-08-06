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
        res = float("inf")
        ans_l = ans_r = 0
        l = 0
        formed = 0
        for r, ch in enumerate(s):
            if ch in d:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == d[ch]:
                    formed += 1

            while l < len(s) and formed == len(d):
                if r - l + 1 < res:
                    res = r - l + 1
                    ans_l = l
                    ans_r = r
                if window.get(s[l], 0) == d.get(s[l], 0) and window.get(s[l], 0) != 0:
                    formed -= 1
                if s[l] in window:
                    window[s[l]] -= 1
                l += 1

        return "" if res == float("inf") else s[ans_l : ans_r + 1]


# @lc code=end
