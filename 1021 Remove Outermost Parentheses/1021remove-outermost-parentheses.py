class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        skip = True
        op = cl = 0
        for ch in s:
            if skip:
                skip = False
                continue
            stack.append(ch)
            if ch == '(':
                op += 1
            if ch == ')':
                cl += 1
            if cl > op:
                stack.pop()
                skip = True
                op = cl = 0
        return ''.join(stack)
            