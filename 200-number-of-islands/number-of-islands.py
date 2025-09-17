from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return []
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        def bfs(start_r: int, start_c: int) -> None:
            q = deque()
            q.append((start_r, start_c))
            visited[start_r][start_c] = True
            while q:
                cur_r, cur_c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = cur_r + dr, cur_c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if visited[nr][nc] or grid[nr][nc] == "0":
                        continue
                    visited[nr][nc] = True
                    q.append((nr, nc))

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    bfs(r, c)
                    res += 1
        return res

