class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []   
        mx = 0
        n = len(heights)

        for i, item in enumerate(heights + [0]):  # добавляем "0" как стоп-кран
            # пока стек не пуст и текущая высота ломает монотонность
            while stack and heights[stack[-1]] > item:
                height = heights[stack.pop()] # 5
                left = stack[-1] if stack else -1
                width = i - left - 1
                # print(i, left)
                mx = max(mx, height * width)
                # print(height * width)
            stack.append(i)
            # print(stack)

        return mx
