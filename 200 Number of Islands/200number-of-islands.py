class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            visited[x][y] = True  

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if not visited[nx][ny] and grid[nx][ny] == '1':  
                        dfs(nx, ny)
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]  
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1
        return cnt