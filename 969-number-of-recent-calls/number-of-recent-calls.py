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
        while self.queue:
            item = self.queue[0]
            if item >= self.start:
                break
            else:
                self.queue.popleft()
        return len(self.queue)
            


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

