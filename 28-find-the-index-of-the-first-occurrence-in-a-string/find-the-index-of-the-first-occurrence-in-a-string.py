#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        i = 1
        length = 0
        while i < len(needle):
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1] # почему после 4 стало 0,
                else:
                    lps[i] = 0
                    i += 1
            # print(length, lps)
        print(lps)

        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
            if j == len(needle):
                break
        else:
            return -1
        return i - len(needle)

        # cnt = 0
        # for i in range(len(haystack) - len(needle) + 1):
        #     for j in range(len(needle)):
        #         if haystack[i + cnt] == needle[j]:
        #             cnt += 1
        #     if cnt == len(needle):
        #         return i
        #     cnt = 0
        return -1


# @lc code=end
