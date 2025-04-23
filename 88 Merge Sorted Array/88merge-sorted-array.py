
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = p2 = 0
        while p1 < m + n and p2 < n:
            if nums1[p1] > nums2[p2]:
                temp = nums1[p1]
                for i in range(p1 + 1, m + n):
                    another = nums1[i]
                    nums1[i] = temp
                    temp = another
                nums1[p1] = nums2[p2]
                p2 += 1
            p1 += 1
        for i in range(p2 + m, m + n):
            nums1[i] = nums2[i - m]
       
        

            
# @lc code=end

