#
# @lc app=leetcode id=2241 lang=python3
#
# [2241] Design an ATM Machine
#

# @lc code=start
from collections import defaultdict
class ATM:

    def __init__(self):
        self.d = defaultdict(int)
        self.back = defaultdict(int)
        self.values = [500, 200, 100, 50, 20]
    def deposit(self, banknotesCount: List[int]) -> None:
        self.d[20] += banknotesCount[0]
        self.d[50] += banknotesCount[1]
        self.d[100] += banknotesCount[2]
        self.d[200] += banknotesCount[3]
        self.d[500] += banknotesCount[4]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i in range(len(self.values)):
            current_banknote = self.values[i]
            if current_banknote <= amount and self.d[current_banknote] > 0:
                target = min(amount // current_banknote, self.d[current_banknote])
                self.back[current_banknote] += target
                res[4 - i] += target
                amount -= current_banknote * target
                self.d[current_banknote] -= target
        if amount == 0:
            self.back.clear()
            return res
        for key in self.back:
            self.d[key] += self.back[key]
        self.back.clear()
        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
# @lc code=end
