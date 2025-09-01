class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        res = list(s)
        d = {}
        
        for i in range(10):
            ans = 0
            for item in res:
                ans += int(item)**2
            if ans == 1:
                return True
            res = list(str(ans))
        return False