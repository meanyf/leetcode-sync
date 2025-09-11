class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        ans = 0
        def dfs(r, c):
            if r > rows - 1 or c > cols - 1: return 0
            if r < 0 or c < 0: return 0
            if grid[r][c] == '0' or (r, c) in visited: return 0
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    ans += 1
        return ans