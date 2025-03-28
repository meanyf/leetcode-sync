class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        d1 = {}
        d2 = {}
        d3 = {}
        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] != '.':
                    d[board[i][j]] = d.get(board[i][j], 0) + 1
                    if d[board[i][j]] > 1:
                        return False
                    
                    if j < 3:
                        d1[board[i][j]] = d1.get(board[i][j], 0) + 1
                        if d1[board[i][j]] > 1:
                            return False
                    elif j < 6:
                        d2[board[i][j]] = d2.get(board[i][j], 0) + 1
                        if d2[board[i][j]] > 1:
                            return False
                    elif j < 9:
                        d3[board[i][j]] = d3.get(board[i][j], 0) + 1
                        if d3[board[i][j]] > 1:
                            return False
            if i == 2:
                d1 = {}
                d2 = {}
                d3 = {}
            if i == 5:
                d1 = {}
                d2 = {}
                d3 = {}
        board = list(map(list, zip(*board)))

        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] != '.':
                    d[board[i][j]] = d.get(board[i][j], 0) + 1
                    if d[board[i][j]] > 1:
                        return False
        
        return True

            