#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.i = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        item = self.stack1[self.i]
        self.i += 1
        return item

    def peek(self) -> int:
        return self.stack1[self.i]

    def empty(self) -> bool:
        if self.i >= len(self.stack1):
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

