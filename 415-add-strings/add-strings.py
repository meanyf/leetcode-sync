#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
from itertools import zip_longest

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        cnt_zeros = abs(len(num1) - len(num2))
        print(cnt_zeros)
        if len(num1) < len(num2):
            num1 = num1.zfill(cnt_zeros + len(num1))
        elif len(num1) > len(num2):
            num2 = num2.zfill(cnt_zeros + len(num2))
        add = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for ch1, ch2 in zip(num1, num2):
            ans = int(ch1) + int(ch2) + add
            add = ans // 10
            res.append(str(ans % 10))
        if add == 1:
            res.append('1')
        return ''.join(list(reversed(res)))


# @lc code=end

