class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    stack = [(r, c)]
                    while stack:
                        i, j = stack.pop()
                        if i < 0 or i >= rows or j < 0 or j >= cols:
                            continue
                        if grid[i][j] == '0' or (i, j) in visited:
                            continue
                        visited.add((i, j))
                        stack.append((i + 1, j))
                        stack.append((i - 1, j))
                        stack.append((i, j + 1))
                        stack.append((i, j - 1))
                    ans += 1
        return ans