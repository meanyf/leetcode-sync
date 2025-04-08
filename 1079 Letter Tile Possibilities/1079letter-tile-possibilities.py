class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        gd = {}
        def GetAllCombinations(nums):
            ans = []
            def Helper(idx, current):
                if idx == len(nums):
                    ans.append(current[:])
                    b([], current)
                    return
                Helper(idx + 1, current + [nums[idx]])
                Helper(idx + 1, current)

            Helper(0, [])
            return ans

        res = []

        def b(current: list, comb: list):
            if len(current) == len(comb):
                res.append(current[:])
                gd[tuple(current)] = True
                return
            
            for ch in comb:
                if current.count(ch) >= comb.count(ch):
                    continue
                if tuple(current + [ch]) in gd: 
                    continue
                current.append(ch)
                b(current, comb)
                current.pop()

        GetAllCombinations(tiles)
        return len(res) - 1