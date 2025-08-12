class Solution:
    def average(self, salary: List[int]) -> float:
        mx = float('-inf')
        mn = float('inf')
        cnt = -2
        res = 0
        for i in range(len(salary)):
            mx = max(mx, salary[i])
            mn = min(mn, salary[i])
            cnt += 1
            res += salary[i]
        return (res - mx - mn) / cnt
