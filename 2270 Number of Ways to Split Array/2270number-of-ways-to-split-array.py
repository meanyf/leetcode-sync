class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        n = len(nums)
        prf = [0] * (n + 1)
        for i in range(1, n + 1):
            prf[i] = prf[i - 1] + nums[i - 1]
        cnt = 0
        for i in range(1, n):
            if prf[i] >= prf[-1] - prf[i]:
                cnt += 1
        return cnt