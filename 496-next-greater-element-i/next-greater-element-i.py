class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        if not nums2:
            return res
        stack = []
        d = {}
        nums2.reverse()
        for item in nums2:
            while stack and stack[-1] < item:
                stack.pop()
            if stack:
                d[item] = stack[-1]
            stack.append(item)
        for i, item in enumerate(nums1):
            if item in d:
                res[i] = d[item]
        return res
        # res = [-1] * len(nums1)
        # for i, num in enumerate(nums1):
        #     x = False
        #     for item in nums2:
        #         if item == num:
        #             x = True
        #         elif x and item > num:
        #             res[i] = item
        #             break
        # return res