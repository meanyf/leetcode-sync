class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res = 0
        rows = len(mat)
        for row in range(rows):
            res += mat[row][row]
            res += mat[rows - 1 - row][row]
        if rows % 2 == 1:
            res -= mat[rows // 2][rows // 2]
        return res