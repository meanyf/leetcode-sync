from collections import defaultdict
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        if not nums:
            return res
        stack = []
        d = defaultdict(list)
        for i in range(2*len(nums) - 1, -1, -1):
            item = nums[i % len(nums)]
            while stack and stack[-1] <= item:
                stack.pop()
            if stack and i < len(nums):
                res[i] = stack[-1]
            stack.append(item)
        # for i, item in enumerate(nums):
        #     if d[item]:
        #         res[i] = d[item].pop()
        return res