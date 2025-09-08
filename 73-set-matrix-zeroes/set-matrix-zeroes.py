class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        zero_rows = set()
        zero_cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in range(len(matrix)):
            if i in zero_rows:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        
        for j in range(len(matrix[0])):
            if j in zero_cols:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        


