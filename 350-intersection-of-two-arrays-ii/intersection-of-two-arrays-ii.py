class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        for item in nums1:
            d[item] = d.get(item, 0) + 1
        for item in nums2:
            if item in d and d[item] > 0:
                res.append(item)
                d[item] -= 1
        return res