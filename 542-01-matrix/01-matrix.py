from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]: return mat
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(mat), len(mat[0])
        res = [[0] * cols for _ in range(rows)]
        q = deque()
        sr = sc = None
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
        visit = set()
        visit.add((sr, sc))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    if mat[nr][nc] == 1:
                        res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))
        return res