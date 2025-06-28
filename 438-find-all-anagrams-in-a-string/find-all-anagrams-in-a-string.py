#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s:
            return []
        d = defaultdict(int)
        res = []
        for item in p:
            d[item] += 1
        l = r = 0
        window = defaultdict(int)
        while r < len(s):
            window[s[r]] += 1
            if s[r] in d and window[s[r]] <= d[s[r]]:
                if r - l + 1 == len(p):
                    res.append(l)
                    if window[s[l]] > 0:
                        window[s[l]] -= 1
                    l += 1
            else:
                while window[s[r]] > d[s[r]]:
                    if window[s[l]] > 0:
                        window[s[l]] -= 1
                    l += 1
            r += 1
        return res
# @lc code=end

