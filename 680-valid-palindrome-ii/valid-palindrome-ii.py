#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        def j(l, r):
            x = l
            cnt = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    cnt += 1
                    if x == len(s) // 2 - 1:
                        r += 1
                    else:
                        l -= 1
                else:
                    r += 1
                    l -= 1
            print(l,r)
            if r == len(s) and l == -1:
                return True
            if cnt == 0:
                return True
        def g(l, r):
            x = l
            cnt = 0

            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    cnt += 1
                    if x == len(s) // 2 - 1:
                        r += 1
                    else:
                        l -= 1
                else:
                    r += 1
                    l -= 1
            if x == len(s) // 2:
                if l == 0 and r == len(s):
                    return True
            if x == len(s) // 2 - 1:
                if l == -1 and r == len(s) - 1:
                    return True
            if r == len(s) and l == -1:
                return True
            
            if cnt == 0:
                return True

        if len(s) % 2 == 0:
            if j(len(s) // 2 - 1, len(s) // 2 - 1):
                return True
            if j(len(s) // 2, len(s) // 2):
                return True
            return False

        else:
            if g(len(s) // 2 - 1, len(s) // 2):
                return True
            if g(len(s) // 2, len(s) // 2 + 1):
                return True
            return False

            

            
# @lc code=end