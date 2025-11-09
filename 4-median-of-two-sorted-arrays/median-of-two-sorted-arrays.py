from math import ceil
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        def feasible(x):
            cnt = 0
            for item in nums1:
                cnt += 1 if item <= x else 0
            for item in nums2:
                cnt += 1 if item <= x else 0
            print('cnt', cnt)
            return cnt
        def bin_search(target):
            ans = None
            lo = min(nums1[0] if nums1 else float('inf'), nums2[0] if nums2 else float('inf'))
            hi = max(nums1[-1] if nums1 else -float('inf'), nums2[-1] if nums2 else -float('inf'))
            while lo <= hi:
                print('lo', 'hi', lo, hi)
                mi = (lo + hi) // 2
                print('mi', mi)
                if feasible(mi) >= target:
                    ans = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            print('ans', ans)
            return ans
        
        target = n // 2
        if n % 2 == 0:
            return (bin_search(target) + bin_search(target + 1)) / 2
        return bin_search(target + 1)