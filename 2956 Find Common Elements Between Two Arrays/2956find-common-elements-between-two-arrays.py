class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d1 = {}
        cnt1 = cnt2 =  0
        for num in nums1:
            d1[num] = d1.get(num, 0) + 1

        d2= {}
        for num in nums2:
            d2[num] = d2.get(num, 0) + 1

        for num in set(nums1):
            if num in d2:
                cnt1 += d1.get(num, 0)
        for num in set(nums2):
            if num in d1:
                cnt2 += d2.get(num, 0)
        return [cnt1, cnt2]