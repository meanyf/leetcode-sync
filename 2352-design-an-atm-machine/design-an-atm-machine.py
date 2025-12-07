class ATM:

    def __init__(self):
        self.d = {500: 0, 200: 0, 100: 0, 50: 0, 20: 0}
        self.banknotes = [500, 200, 100, 50, 20]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, item in enumerate(banknotesCount[::-1]):
            self.d[self.banknotes[i]] = self.d.get(self.banknotes[i], 0) + item
    def withdraw(self, amount: int) -> List[int]:
        res = []
        original = self.d.copy()
        for item in self.banknotes:
            total = 0
            if self.d[item] > 0:
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