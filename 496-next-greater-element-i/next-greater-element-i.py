class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            x = False
            for item in nums2:
                if item == num:
                    x = True
                elif x and item > num:
                    res[i] = item
                    break
        return res