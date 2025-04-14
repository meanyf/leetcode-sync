class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        ids = [i for i, num in enumerate(nums) if num == key]
        res = []
        for i in range(len(nums)):
            for idx in ids:
                if abs(idx - i) <= k:
                    res.append(i)
                    break
        res.sort()
        return res