class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = [[None] * rows for _ in range(cols)]
        rows, cols = cols, rows
        for row in range(rows):
            for col in range(cols):
                res[row][col] = matrix[col][row]   
        return res

