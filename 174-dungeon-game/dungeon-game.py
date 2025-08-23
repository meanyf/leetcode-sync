from functools import cache
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        grid = dungeon
        m = len(grid)
        n = len(grid[0])
        @cache
        def run(x, y):
            if x >= m or y >= n:
                return -float('inf')
            if x == m - 1 and y == n - 1:
                return grid[x][y]
            item = grid[x][y]
            down_mn = run(x + 1, y)
            right_mn = run(x, y + 1)
            if down_mn > right_mn:
                return min(item, item + down_mn)
            else:
                return min(item, item + right_mn)


        bst = run(0, 0)
        if bst > 0:
            return 1
        return 1 - bst
            