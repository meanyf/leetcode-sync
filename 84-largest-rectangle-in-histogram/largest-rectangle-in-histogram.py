class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nums = heights
        stack = []
        mx = 0
        res = [len(nums)] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            item = nums[i]
            while stack and nums[stack[-1]] >= item:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(i)

        stack = []
        res2 = [-1] * len(nums)
        for i in range(len(nums)):
            item = nums[i]
            while stack and nums[stack[-1]] >= item:
                stack.pop()
            if stack:
                res2[i] = stack[-1]
            stack.append(i)
        mx = 0
        for i, h in enumerate(heights):
            mx = max(mx, h * (res[i] - res2[i] - 1))
        return mx