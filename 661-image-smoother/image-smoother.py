import math
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        dirs = [(0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (1, 0), (-1, 0), (0, 0)]

        cols = len(img[0])
        res = [[None] * cols for row in range(len(img))]
        for row in range(len(img)):
            for col in range(len(img[0])):
                ans = cnt = 0
                for x, y in dirs:
                    if -1 < row + y < len(img) and -1 < col + x < len(img[0]):
                        ans += (img[row + y][col + x]) 
                        cnt += 1
                res[row][col] = math.floor(ans / cnt)
        return res
                