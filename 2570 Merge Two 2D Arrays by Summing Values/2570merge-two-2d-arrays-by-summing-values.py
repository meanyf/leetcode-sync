class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        l = r = 0
        lst = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l][0] < nums2[r][0]:
                lst.append(nums1[l][0])
                l += 1
            else:
                lst.append(nums2[r][0])
                r += 1
                
        if l < len(nums1):
            lst.extend([num[0] for num in nums1[l:]])

        if r < len(nums2):
            lst.extend([num[0] for num in nums2[r:]])
            print(lst)

        d1 = {}
        for num in nums1:
            d1[num[0]] = num[1]
        d2 = {}
        for num in nums2:
            d2[num[0]] = num[1]
        
        
        res = []
        lst = sorted(set(lst))
        for num in lst:
            if num in d1 or num in d2:
                res.append([num, d1.get(num, 0) + d2.get(num, 0)])
        return res