#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            try:
                num = int(item)
                stack.append(num)
            except ValueError:
                num1 = stack.pop()
                num2 = stack.pop() 
                if item == '+':
                    stack.append(num1 + num2)
                if item == '-':
                    stack.append(num2 - num1)
                if item == '*':
                    stack.append(num1 * num2)
                if item == '/':
                    stack.append(int(num2 / num1))
                
        return stack[-1]

# @lc code=end

