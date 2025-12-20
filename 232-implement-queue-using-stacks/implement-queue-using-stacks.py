class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack2:
            self.stack1.append(x)
        else:
            self.stack2.append(x)

    def pop(self) -> int:
        if not self.stack2:
            ans = self.stack1[0]
            for i in range(1, len(self.stack1)):
                self.stack2.append(self.stack1[i])
            self.stack1.clear()
            return ans
        else:
            ans = self.stack2[0]
            for i in range(1, len(self.stack2)):
                self.stack1.append(self.stack2[i])
            self.stack2.clear()
            return ans

    def peek(self) -> int:
        return self.stack1[0] if self.stack1 else self.stack2[0]

    def empty(self) -> bool:
        return True if not self.stack1 and not self.stack2 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()