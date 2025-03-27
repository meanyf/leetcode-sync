class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for k in d:
            if d[k] == len(nums) // 2:
                return k