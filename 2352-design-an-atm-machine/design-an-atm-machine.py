class ATM:

    def __init__(self):
        self.banknotes = [500, 200, 100, 50, 20]
        self.counts = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.counts[i] += banknotesCount[len(banknotesCount) - 1 - i]

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i in range(len(self.banknotes)):
            total = min(amount // self.banknotes[i], self.counts[i])
            amount -= total * self.banknotes[i]
            res[len(res) - 1 - i] = total
        if amount != 0:
            return [-1]
        for i in range(len(res)):
            self.counts[i] -= res[len(res) - 1 - i]
        return res

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)