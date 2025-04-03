class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix = []
        for i in range(len(mat) + 1):
            prefix.append([0] * (len(mat[0]) + 1))

        for row in range(1, len(mat) + 1):
            for col in range(1, len(mat[0]) + 1):
                prefix[row][col] = prefix[row][col - 1] + prefix[row - 1][col] - prefix[row - 1][col - 1] + mat[row - 1][col - 1]

        answer = []
        for i in range(len(mat)):
            answer.append([0] * len(mat[0]))
                        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                r1 = max(0, i - k)
                r2 = min(len(mat) - 1, i + k)
                c1 = max(0, j - k)
                c2 = min(len(mat[0]) - 1, j + k)
                answer[i][j] = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
        return answer
