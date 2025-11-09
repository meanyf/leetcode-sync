from math import ceil
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        def feasible(x):
            return bisect_right(nums1, x) + bisect_right(nums2, x)
        def bin_search(target):
            ans = None
            lo = min(nums1[0] if nums1 else float('inf'), nums2[0] if nums2 else float('inf'))
            hi = max(nums1[-1] if nums1 else -float('inf'), nums2[-1] if nums2 else -float('inf'))
            while lo <= hi:
                mi = (lo + hi) // 2
                if feasible(mi) >= target:
                    ans = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            return ans
        target = n // 2
        if n % 2 == 0:
            return (bin_search(target) + bin_search(target + 1)) / 2
        return bin_search(target + 1)