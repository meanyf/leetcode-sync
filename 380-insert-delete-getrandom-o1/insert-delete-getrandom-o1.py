#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random

class RandomizedSet:

    def __init__(self):
        self.d = dict()
        self.id = 0
        self.lst = []

    def insert(self, val: int) -> bool:
        x = None
        if val in self.d:
            x = False
        else:
            self.d[val] = self.id
            self.lst.append(val)
            x = True
            self.id += 1
        return x

    def remove(self, val: int) -> bool:
        x = None
        if val in self.d:
            x = True
            id = self.d[val]
            self.lst[id] = self.lst[-1]
            self.d[self.lst[-1]] = id
            self.lst.pop()
            del self.d[val]
            self.id -= 1
        else:
            x = False
        return x

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

