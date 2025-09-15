class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = set()
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in visited:
                    stack = [(i, j)]
                    isRegion = True
                    region = []
                    while stack:
                        cur_i, cur_j = stack.pop()
                        if (cur_i, cur_j) in visited or board[cur_i][cur_j] == 'X':
                            continue
                        visited.add((cur_i, cur_j))
                        region.append((cur_i, cur_j))
                        for di, dj in dirs:
                            ni, nj = di + cur_i, dj + cur_j
                            if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                                isRegion = False
                                continue
                            if board[ni][nj] == 'O' and (ni, nj) not in visited:
                                stack.append((ni, nj))
                    if isRegion:
                        for cur_i, cur_j in region:
                            board[cur_i][cur_j] = 'X'
                
