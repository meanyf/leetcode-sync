from functools import cache
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        grid = matrix
        m = len(grid)
        n = len(grid[0])
        bst = 0
        @cache
        def run(x, y):
            nonlocal bst
            if x >= m or y >= n:
                return 0
            item = grid[x][y]
            side = min(run(x + 1, y), run(x, y + 1), run(x + 1, y + 1)) + item
            if item == 0:
                side = 0
            bst += side
            return side
            
        run(0, 0)
        return bst