class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = set(nums3)
        return list((s1 & s2) | (s1 & s3) | (s2 & s3))