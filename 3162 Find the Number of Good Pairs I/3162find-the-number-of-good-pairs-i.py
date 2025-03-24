class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        cnt = 0
        d = {}
        for j in range(len(nums2)):
            d[j] = nums2[j] * k
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % d[j] == 0:
                    cnt +=1
        return cnt
