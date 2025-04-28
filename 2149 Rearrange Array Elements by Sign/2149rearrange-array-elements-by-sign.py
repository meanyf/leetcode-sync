class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        lst1 = [x for x in nums if x > 0]
        lst2 = [x for x in nums if x < 0]
        n = len(nums)
        lst = [0] * n
        j1 = j2 = 0
        for i in range(n):
            if i % 2 == 0:
                lst[i] = (lst1[j1])
                j1 += 1
            else:
                lst[i] = (lst2[j2])
                j2 += 1
        return lst
            