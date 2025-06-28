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
        d2 = defaultdict(int)
        target = 0
        while l < len(s) and r < len(s):
            d2[s[r]] += 1
            target += 1
            if s[r] in d and d2[s[r]] <= d[s[r]]:
                if target == len(p):
                    res.append(l)
                    if d2[s[l]] > 0:
                        d2[s[l]] -= 1
                    l += 1
                    target -= 1
            else:
                if s[r] not in d:
                    l = r + 1
                    d2.clear()
                    target = 0
                else:
                    el = s[r]
                    while d2[el] != d[el]:
                        if d2[s[l]] > 0:
                            d2[s[l]] -= 1
                            target -= 1
                        l += 1
            r += 1
        return res
# @lc code=end

