class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nums = heights
        if len(nums) == 1:
            return nums[0]
        stack = []
        mx = 0
        res = [-1] * len(nums)
        
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
        print(res)
        print(res2)
        mx = 0
        for i, item in enumerate(nums):
            a = res[i] 
            b = res2[i]
            if a == -1 and b == -1:
                mx = max(mx, item * len(nums))
            elif a == -1 and b != -1:
                mx = max(mx, item * (len(nums) - b - 1))
            elif a != -1 and b == -1:
                mx = max(mx, item * a)
            else:
                mx = max(mx, (res[i] - res2[i] - 1) * item)
            print(mx)
        return mx