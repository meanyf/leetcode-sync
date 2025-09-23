class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        grid = mat
        if not grid or not grid[0]: return 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited[r][c] = True
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 0 or visited[nr][nc]:
                        continue
                    if grid[r][c] != 0:
                        grid[nr][nc] = grid[r][c] + 1
                    visited[nr][nc] = True
                    q.append((nr, nc))
        return grid
                    