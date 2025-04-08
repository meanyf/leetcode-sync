class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        gb = {}
        def b(start, current: list):
            d = {}
            for item in current:
                d[item] = d.get(item, 0) + 1
            if frozenset(d.items()) not in gb:
                res.append(current[:])
            gb[frozenset(d.items())] = True

            for i in range(start, len(nums)):
                current.append(nums[i])
                b(i + 1, current)
                current.pop()
        b(0, [])
        return list(res)