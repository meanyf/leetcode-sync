class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        d = {}
        def b(current: list):
            if len(current) == len(nums):
                res.append(current[:])
                d[tuple(current)] = True
                return
            for num in nums:
                if current.count(num) == nums.count(num):
                    continue
                if tuple(current + [num]) in d:
                    continue
                current.append(num)
                b(current)
                current.pop()
        b([])
        return res
        