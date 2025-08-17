class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[None] * n for _ in range(n)]

        top = left = 0
        bottom = right = n - 1
        cnt = 1
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res[top][col] = cnt
                cnt += 1
            top += 1

            for row in range(top, bottom + 1):
                res[row][right] = cnt
                cnt += 1
            right -= 1

            if top <= bottom:
                for col in range(right, left - 1, - 1):
                    res[bottom][col] = cnt
                    cnt += 1
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res[row][left] = cnt 
                    cnt += 1
                left += 1
        
        return res