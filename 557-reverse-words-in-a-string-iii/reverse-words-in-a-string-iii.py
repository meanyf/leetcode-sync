#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        start = end = 0
        for i in range(len(s)):
            if s[i] == ' ':
                end = i - 1
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                start = i + 1
        
        i = len(s) - 1
        while i > 0 and s[i] != ' ':
            i -= 1
        if len(s) >= 1 and s[i] == ' ':
            i += 1  
        end = len(s) - 1
        while i < end:
            s[i], s[end] = s[end], s[i]
            i += 1
            end -= 1
        return ''.join(s)



# @lc code=end

