class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            visited.add((i, j))
            stack = [(i, j)]
            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '1' and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            stack.append((nr, nc))

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        return res