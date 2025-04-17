class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for item in logs:
            if stack and item == '../':
                stack.pop()
            elif item != './' and item != '../':
                stack.append(item)
        print(stack)
        return len(stack)