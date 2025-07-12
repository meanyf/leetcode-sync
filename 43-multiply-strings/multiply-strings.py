#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [ord(ch) - 48 for ch in reversed(num1)]
        num2 = [ord(ch) - 48 for ch in reversed(num2)]
        total = []
        for i, item in enumerate(num2):
            res = [0] * i
            add = 0
            for ch in num1:
                ans = ch * item + add
                add = ans // 10
                res.append(ans % 10)
            if add:
                res.append(add)
            total.append(res)
        total.reverse()
        for i in range(len(total)):
            total[i].extend([0] * i)
        res = list(total[0])
        for item in total[1:]:
            add = 0
            if len(item) < len(res):
                item.extend([0] * (len(res) - len(item)))
            for i, (ch1, ch2) in enumerate(zip(item, res)):
                ans = ch1 + ch2 + add
                add = ans // 10
                res[i] = (ans % 10)
            if add:
                res.append(1)
        if set(res) == {0}: return '0'
        return ''.join(map(str, reversed(res)))


        # res = []
        # i = 0
        # cnt_zeros = abs(len(num1) - len(num2))
        # print(cnt_zeros)
        # if len(num1) < len(num2):
        #     num1 = num1.zfill(cnt_zeros + len(num1))
        # elif len(num1) > len(num2):
        #     num2 = num2.zfill(cnt_zeros + len(num2))
        # add = 0
        # print(num1, num2)
        # num1 = num1[::-1]
        # num2 = num2[::-1]
        # for ch1, ch2 in zip(num1, num2):
        #     ans = int(ch1) + int(ch2) + add
        #     add = ans // 10
        #     res.append(str(ans % 10))
        # if add == 1:
        #     res.append('1')
        # return ''.join(list(reversed(res)))
# @lc code=end

