class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num != 0:
                d[num] = d.get(num, 0) + 1
        return len(list(d.keys()))