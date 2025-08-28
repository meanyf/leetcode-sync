import math
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        dy = coordinates[1][1] - y1
        dx = coordinates[1][0] - x1
        if dx == 0:
            k = None
        else:
            k = dy / dx
        for i in range(2, len(coordinates)):
            x2 = coordinates[i][0]
            y2 = coordinates[i][1]
            dy = y2 - y1
            dx = x2 - x1
            if dx == 0:
                cur_k = None
            else:
                cur_k = dy / dx
            if cur_k is None and k is not None:
                return False
            if k is None and cur_k is not None:
                return False
            if cur_k != k:
                return False
        return True
