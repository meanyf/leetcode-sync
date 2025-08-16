#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        for row in matrix:
            print(row)
        ord = 0
        cnt = 0
        l = len(matrix) * len(matrix[0])
        print(len(matrix) * len(matrix[0]))
        res = []
        row = col = 0

        min_row = 0
        min_col = 0
        max_row = len(matrix) - 1
        max_col = len(matrix[0]) - 1
        while cnt < l:
            ord = ord % 4
            print(row, col)
            print(res)
            if ord == 0:
                res.append(matrix[row][col])
                col += 1
            elif ord == 1:
                res.append(matrix[row][col])
                row += 1
                ...
            elif ord == 2:
                res.append(matrix[row][col])
                col -= 1
                ...
            elif ord == 3:
                res.append(matrix[row][col])
                row -= 1
                ...
            cnt += 1

            if col > max_col and ord == 0:
                row += 1
                ord += 1
                col = max_col
                min_row += 1
            if row > max_row and ord == 1:
                col -= 1
                ord += 1
                max_col -= 1
                row = max_row
            if col < min_col and ord == 2:
                row -= 1
                ord += 1
                max_row -= 1
                col = min_col
            if row < min_row and ord == 3:
                col += 1
                ord += 1
                min_col += 1
                row = min_row
        return res


# @lc code=end
