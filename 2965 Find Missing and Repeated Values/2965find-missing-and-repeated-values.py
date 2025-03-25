class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        d = {}
        a = b = None
        for i in range(n):
            for j in range(n):
                d[grid[i][j]] = d.get(grid[i][j], 0) + 1
                if d[grid[i][j]] > 1:
                    a = grid[i][j]
        
        cnt = 1
        for i in range(n * n):
            if cnt not in d:
                b = cnt
            cnt += 1
        return [a, b]
        

