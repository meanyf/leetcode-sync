class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def dfs(i, j):
            visited.add((i, j))
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if grid[ni][nj] == '1' and (ni, nj) not in visited:
                            visited.add((ni, nj))
                            stack.append((ni, nj))

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        return res