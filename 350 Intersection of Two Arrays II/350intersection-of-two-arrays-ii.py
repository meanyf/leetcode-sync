class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        d = {}
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        res = []
        for num in nums2:
            if num in d and d[num] > 0:
                res.append(num)
                d[num] -= 1
        return res

        