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
                row, col = stack.pop()
                for dr, dc in dirs:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == '1' and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            stack.append((nr, nc))

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        return res