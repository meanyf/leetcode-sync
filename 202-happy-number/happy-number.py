class Solution:
    def isHappy(self, n: int) -> bool:
        res = str(n)
        used = set()
        while True:
            ans = 0
            ans = sum(int(item)**2 for item in res)
            if ans in used:
                return False
            used.add(ans)
            if ans == 1:
                return True
            res = str(ans)
        return False