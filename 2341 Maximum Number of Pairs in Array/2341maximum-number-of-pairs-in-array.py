class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        d = {}
        cnt = 0
        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d[num] == 2:
                d[num] = 0
                cnt += 1
        ans = sum(d.values())
        return [cnt, ans]