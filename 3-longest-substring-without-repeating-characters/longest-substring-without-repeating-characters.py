#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l = 0
        mx = 0
        last = 0
        for r, ch in enumerate(s):
            
            if ch in d:
                last = max(d[ch] + 1, last)
                l = last
                

            d[ch] = r
            
            mx = max(mx, r - l + 1)
        return mx

# @lc code=end

