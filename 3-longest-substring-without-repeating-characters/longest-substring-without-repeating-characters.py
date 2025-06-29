#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        l = 0
        mx = 0
        for r, ch in enumerate(s):
            d[ch] += 1

            while d[ch] > 1:
                d[s[l]] -= 1
                l += 1
            
            mx = max(mx, r - l + 1)
        return mx

# @lc code=end

