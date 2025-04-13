class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = set()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        s = set(nums1)
        for num in nums2:
            if num in s:
                res.add(num)
        return list(res)