#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cnt = 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + cnt] == needle[j]:
                    cnt += 1
            if cnt == len(needle):
                return i 
            cnt = 0
        return -1


# @lc code=end
