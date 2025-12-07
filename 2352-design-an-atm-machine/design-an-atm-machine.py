class ATM:

    def __init__(self):
        self.d = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0}
        self.banknotes = [500, 200, 100, 50, 20]

    def deposit(self, banknotesCount: List[int]) -> None:
        for cnt, banknote in zip(banknotesCount[::-1], self.banknotes):
            self.d[banknote] = self.d[banknote] + cnt

    def withdraw(self, amount: int) -> List[int]:
        res = []
        original = self.d.copy()
        for item in self.banknotes:
            total = min(amount // item, self.d[item])
            amount -= total * item
            self.d[item] -= total
            res.append(total)
        if amount == 0:
            return res[::-1]
        else:
            self.d = original
            return [-1]

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)