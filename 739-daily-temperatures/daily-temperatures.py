class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums = temperatures
        res = [0] * len(nums)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            item = nums[i]
            while stack and nums[stack[-1]] <= item:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res