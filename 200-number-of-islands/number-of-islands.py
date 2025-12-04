class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                visited.add((i, j))
                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == '1' and (ni, nj) not in visited:
                            stack.append((ni, nj))
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        return res