class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(s):
            stack = []
            for ch in s:
                if stack and ch == '#':
                    stack.pop()
                elif ch != '#':
                    stack.append(ch)
            return stack
        return f(s) == f(t)
        
        