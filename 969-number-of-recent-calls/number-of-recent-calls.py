#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
from collections import deque
class RecentCounter:

    def __init__(self):
        self.queue = deque([])
        self.start = 0

    def ping(self, t: int) -> int:
        self.start = t - 3000
        self.queue.append(t)
        i = 0
        cnt = 0
        k = 0
        while i < len(self.queue):
            item = self.queue[i]
            if item >= self.start:
                break
            i += 1
        for _ in range(min(i, len(self.queue))):
            self.queue.popleft()
        return len(self.queue)
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

