#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random

class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        x = None
        if val in self.s:
            x = False
        else:
            x = True
        self.s.add(val)
        return x

    def remove(self, val: int) -> bool:
        x = None
        if val in self.s:
            x = True
            self.s.remove(val)
        else:
            x = False
        return x

    def getRandom(self) -> int:
        return random.choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

