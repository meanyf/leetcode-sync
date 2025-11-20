class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        mx = 0
        sm = 0
        d2 = {}
        for i, item in enumerate(nums):
            sm += 1 if item == 0 else -1
            d[i] = d.get(i, 0) + sm
            if d[i] in d2:
                mx = max(mx, i - d2[sm])
            else:
                d2[sm] = i
            if sm == 0:
                mx = max(mx, i + 1)
        return mx