class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        if len(grid) < 2 or len(grid[0]) < 2:
            return []
        res = []
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, 0), (0, -1), (1, 0), (1, 1), (1, -1)]
        for i in range(1, len(grid) - 1):
            res.append([])
            for j in range(1, len(grid[0]) - 1):
                mx = -float('inf')
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    mx = max(mx, grid[ni][nj])
                res[-1].append(mx)
        return res