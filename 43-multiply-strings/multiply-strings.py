#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        total = []
        for i, item in enumerate(num2):
            res = ['0'] * i
            add = 0
            for ch in num1:
                ans = int(ch) * int(item) + add
                add = ans // 10
                res.append(str(ans % 10))
            if add:
                res.append(str(add))
            total.append(res)
            # print(res)
        total.reverse()
        for i in range(len(total)):
            total[i].extend(['0'] * i)
        res = list(total[0])
        for item in total[1:]:
            add = 0
            cnt_zeros = abs(len(res) - len(item))
            item = ''.join(item)
            if len(res) > len(item):
                item = item.ljust(cnt_zeros + len(item), '0')
            for i, (ch1, ch2) in enumerate(zip(item, res)):
                print(ch1, ch2)
                ans = int(ch1) + int(ch2) + add
                add = ans // 10
                res[i] = (str(ans % 10))
            if add == 1:
                res.append('1')
        if set(res) == {"0"}: return '0'
        return ''.join(list(reversed(res)))

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

