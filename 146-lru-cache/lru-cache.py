#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.od[key] = value
        self.od.move_to_end(key)
        if len(self.od) > self.capacity:
            self.od.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

