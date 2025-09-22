from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
        res = 0
        while q:
            level = []
            while q:
                r, c = q.popleft()
                visited[r][c] = True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if visited[nr][nc]:
                        continue
                    if grid[nr][nc] == 1:
                        level.append((nr, nc))
                        visited[nr][nc] = True
            q.extend(level)
            res += 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    return -1
        return res - 1 if res > 0 else 0
            
                
