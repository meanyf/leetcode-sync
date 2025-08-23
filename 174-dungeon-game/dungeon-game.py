from functools import cache
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        grid = dungeon
        m = len(grid)
        n = len(grid[0])
        for row in grid:
            print(row)
        @cache
        def run(x, y):
            if x >= m or y >= n:
                return float('inf'), -float('inf')
            if x == m - 1 and y == n - 1:
                return grid[x][y], grid[x][y]
            item = grid[x][y]
            down, down_mn = run(x + 1, y)
            right, right_mn = run(x, y + 1)
            down += item
            right += item
            if down_mn > right_mn:
                return down, min(item, item + down_mn)
            else:
                return right, min(item, item + right_mn)


        dd, bst = run(0, 0)
        print(bst)
        if bst > 0:
            return 1
        return 1 - bst
            