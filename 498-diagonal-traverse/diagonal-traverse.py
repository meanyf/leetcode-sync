class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        row = col = 0
        direction = 1
        while 0 <= row < len(mat) and 0 <= col < len(mat[0]):
            res.append(mat[row][col])
            row -= direction
            col += direction
            if not (0 <= row < len(mat) and 0 <= col < len(mat[0])):
                direction *= -1
                row -= direction
                col += direction
                if direction == -1:
                    if col + 1 < len(mat[0]):
                        col += 1
                    else:
                        row += 1
                else:
                    if row + 1 < len(mat):
                        row += 1
                    else:
                        col += 1
        return res