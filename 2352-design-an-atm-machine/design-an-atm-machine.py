class ATM:

    def __init__(self):
        self.banknotes = [500, 200, 100, 50, 20]
        self.counts = {banknote:0 for banknote in self.banknotes}

    def deposit(self, banknotesCount: List[int]) -> None:
        for cnt, banknote in zip(banknotesCount[::-1], self.banknotes):
            self.counts[banknote] += cnt

    def withdraw(self, amount: int) -> List[int]:
        res = []
        original = self.counts.copy()
        for banknote in self.banknotes:
            total = min(amount // banknote, self.counts[banknote])
            amount -= total * banknote
            self.counts[banknote] -= total
            res.append(total)
        if amount == 0:
            return res[::-1]
        else:
            self.counts = original
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)