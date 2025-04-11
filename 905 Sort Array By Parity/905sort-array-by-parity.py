class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res1 = []
        res2 = []
        for num in nums:
            if num % 2 == 0:
                res1.append(num)
            else:
                res2.append(num)
        return res1 + res2