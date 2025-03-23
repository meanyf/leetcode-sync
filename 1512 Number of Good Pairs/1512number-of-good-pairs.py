class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        cnt = 0
        length = len(nums)
        d = {}
        for i in range(length):
            d[nums[i]] = d.get(nums[i], 0) + 1
        for k in d:
            cnt += d[k] * (d[k] - 1) // 2
        return cnt
