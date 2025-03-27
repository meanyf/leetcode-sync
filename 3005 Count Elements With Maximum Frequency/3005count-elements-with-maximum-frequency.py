class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        m = max(d.values())
        cnt = 0
        for k in d:
            cnt += 1 if d[k] == m else 0
        return m * cnt