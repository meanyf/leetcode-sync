class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        mx = sm = 0
        for i, item in enumerate(nums):
            sm += 1 if item == 0 else -1
            if sm in d:
                mx = max(mx, i - d[sm])
            else:
                d[sm] = i
            if sm == 0:
                mx = max(mx, i + 1)
        return mx