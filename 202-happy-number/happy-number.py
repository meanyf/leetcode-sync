class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        res = list(s)
        used = set()
        while True:
            ans = 0
            item = str(res)
            if item in used:
                return False
            used.add(item)
            for item in res:
                ans += int(item)**2
            if ans == 1:
                return True
            res = list(str(ans))
        return False