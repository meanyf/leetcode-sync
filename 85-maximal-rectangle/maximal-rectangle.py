class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = [0] * len(matrix[0])
        mx = 0
        for row in matrix:
            stack = []
            for i, item in enumerate(row):
                if item == '0':
                    res[i] = 0
                else:
                    res[i] += 1
                    n = len(res)
            for i, item in enumerate(res + [0]): 
                while stack and res[stack[-1]] > item:
                    height = res[stack.pop()] 
                    left = stack[-1] if stack else -1
                    width = i - left - 1
                    mx = max(mx, height * width)
                stack.append(i)
        return mx