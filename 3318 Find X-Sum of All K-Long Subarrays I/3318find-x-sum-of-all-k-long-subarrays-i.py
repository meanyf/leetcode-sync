class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        d = {}
        res = [0] * (n - k + 1)
        for i in range(k):
            d[nums[i]] = d.get(nums[i], 0) + 1
        l = 0 
        r = k - 1
        for i in range(n - k + 1):
            d = dict(sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True))
            ans = 0
            for val, freq in list(d.items())[:x]:
                ans += val * freq
            res[i] = ans
            l += 1
            r += 1
            d[nums[l - 1]] -= 1
            if r < n:
                d[nums[r]] = d.get(nums[r], 0) + 1
        return res
        # while r < n:
