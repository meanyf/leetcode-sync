from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return -1
        rows, cols = len(grid), len(grid[0])
        res = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        visited = [[False] * cols for _ in range(rows)]
        def bfs(start_r, start_c):
            if grid[start_r][start_c] == 1: return -1
            if grid[start_r][start_c] == 0 and rows == 1 and cols == 1: return 1
            dist = 1
            q = deque()
            q.append((start_r, start_c, dist))
            while q:
                r, c, dist = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if visited[nr][nc] or grid[nr][nc] == 1:
                        continue
                    if nr == rows - 1 and nc == cols - 1:
                        return dist + 1
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
            return -1
        return bfs(0, 0)