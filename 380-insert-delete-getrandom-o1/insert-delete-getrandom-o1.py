from random import randint, choice
class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.d: return False
        self.d[val] = len(self.d)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.d: return False
        i = self.d[val]
        prev_last_val = self.lst[-1]
        self.lst[i] = prev_last_val 
        self.d[prev_last_val] = i
        self.lst.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()