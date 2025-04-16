class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch == 'C' and stack:
                stack.pop()
            elif ch == 'D':
                stack.append(stack[-1] * 2)
            elif ch == '+' and len(stack) > 1:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(ch))
        print(stack)
        return sum(stack)