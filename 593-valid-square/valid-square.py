class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        side1 = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
        side2 = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2
        side = min(side1, side2)
        print(side)
        res = [p1, p2, p3, p4]
        for item in res:
            cnt_side = cnt_diag = 0
            for p in res:
                ans = (item[0] - p[0])**2 + (item[1] - p[1])**2
                if ans == side:
                    cnt_side += 1
                elif ans == 2*side:
                    cnt_diag += 1
            print(cnt_side,cnt_diag)
            if not (cnt_side == 2 and cnt_diag == 1):
                return False
        return True
