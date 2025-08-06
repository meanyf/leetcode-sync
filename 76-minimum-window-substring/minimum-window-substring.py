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
        ans = ""
        window = {}
        win2 = {}
        res = float("inf")
        l = 0
        for r, ch in enumerate(s):
            if l > r: break
            if ch in d:
                window[ch] = window.get(ch, 0) + 1

            if len(window) == len(d):
                x = True
                while x and l < len(s):
                    for item in d:
                        if d[item] > window[item]:
                            x = False
                            break
                    if x is False: break
                    if r - l + 1 < res:
                        res = r - l + 1
                        ans = s[l : r + 1]
                    if s[l] in window:
                        window[s[l]] -= 1
                    l += 1
                    # print(s[l : r + 1])

        return ans


# @lc code=end