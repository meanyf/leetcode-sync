class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch != stack[-1] and (ch.upper() == stack[-1] or ch.lower() == stack[-1]):
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
