#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat
        res = [[None] * c for _ in range(r)]
        mat_row = mat_col = 0
        for row in range(r):
            for col in range(c):
                if mat_col == cols:
                    mat_col = 0
                    mat_row += 1
                res[row][col] = mat[mat_row][mat_col] 
                mat_col += 1
        return res
# @lc code=end

