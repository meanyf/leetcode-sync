class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    res.append((row, col))
        
        for row, col in res:
            for i in range(len(matrix)):
                matrix[i][col] = 0
            
            for j in range(len(matrix[row])):
                matrix[row][j] = 0