class ATM:

    def __init__(self):
        self.banknotes = [500, 200, 100, 50, 20]
        self.counts = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, cnt in enumerate(banknotesCount[::-1]):
            self.counts[i] += cnt

    def withdraw(self, amount: int) -> List[int]:
        res = []
        for i, banknote in enumerate(self.banknotes):
            total = min(amount // banknote, self.counts[i])
            amount -= total * banknote
            res.append(total)
        if amount == 0:
            for i in range(len(res)):
                self.counts[i] -= res[i]
            return res[::-1]
        else:
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)