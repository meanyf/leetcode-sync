class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = list(int(x) for x in str(n))
        ans_sum = sum(res)
        product = 1
        for item in res:
            product *= item
        return product - ans_sum