#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ord = cnt = 0
        l = len(matrix) * len(matrix[0])
        res = []
        row = col = 0
        min_row = min_col = 0
        max_row = len(matrix) - 1
        max_col = len(matrix[0]) - 1
        while min_row <= max_row and min_col <= max_col:
            for c in range(min_col, max_col + 1):
                res.append(matrix[min_row][c])
            min_row += 1
            for r in range(min_row, max_row + 1):
                res.append(matrix[r][max_col])
            max_col -= 1

            if min_row <= max_row:
                for c in range(max_col, min_col - 1, -1):
                    res.append(matrix[max_row][c])
                max_row -= 1
            if min_col <= max_col:
                for r in range(max_row, min_row - 1, -1):
                    res.append(matrix[r][min_col])
                min_col += 1
            # ord = ord % 4
            # if ord == 0:
            #     col += 1
            # elif ord == 1:
            #     row += 1
            # elif ord == 2:
            #     col -= 1
            # elif ord == 3:
            #     row -= 1

            # if col > max_col and ord == 0:
            #     ord += 1
            #     row += 1
            #     col = max_col
            #     min_row += 1
            # elif row > max_row and ord == 1:
            #     col -= 1
            #     ord += 1
            #     max_col -= 1
            #     row = max_row
            # elif col < min_col and ord == 2:
            #     row -= 1
            #     ord += 1
            #     max_row -= 1
            #     col = min_col
            # elif row < min_row and ord == 3:
            #     col += 1
            #     ord += 1
            #     min_col += 1
            #     row = min_row
#
            # cnt += 1
        return res


# @lc code=end
