from collections import defaultdict
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums1 = nums[:]
        nums2 = nums[:] + nums[:]
        
        res = [-1] * len(nums1)
        if not nums2:
            return res
        stack = []
        d = defaultdict(list)
        for item in reversed(nums2):
            while stack and stack[-1] <= item:
                stack.pop()
            if stack:
                d[item].append(stack[-1])
            stack.append(item)
        print(d)
        for i, item in enumerate(nums1):
            if d[item]:
                res[i] = d[item].pop()
        d = {}
        # for item in nums2:
        #     while stack and stack[-1] <= item:
        #         stack.pop()
        #     if stack:
        #         d[item] = stack[-1]
        #     stack.append(item)
        # for i, item in enumerate(nums1):
        #     if item in d and res[i] == -1:
        #         res[i] = d[item]
        return res