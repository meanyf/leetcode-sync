#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] = False
            else:
                d[s[i]] = i
        for k in d:
            if d[k] is not False:
                return d[k]
        return -1
# @lc code=end

