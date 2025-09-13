class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i + 1 >= rows:
                        ans += 1
                    elif grid[i + 1][j] == 0:
                        ans += 1

                    if j + 1 >= cols:
                        ans += 1
                    elif grid[i][j + 1] == 0:
                        ans += 1

                    if i - 1 < 0:
                        ans += 1
                    elif grid[i - 1][j] == 0:
                        ans += 1

                    if j - 1 < 0:
                        ans += 1
                    elif grid[i][j - 1] == 0:
                        ans += 1
        return ans