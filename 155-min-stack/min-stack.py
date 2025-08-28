class MinStack:

    def __init__(self):
        self.stack = []
        self.mn = float('inf')
        self.prev = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.mn:
            self.prev.append(self.mn)
        self.mn = min(val, self.mn)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mn:
            self.mn = self.prev.pop() if self.prev else float('inf')
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()