class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        res = [0] * n
        flag = False
        if k == 0:
            return res
        if k < 0:
            code.reverse()
            k *= -1
            flag = True
        code += code
        ans = sum(code[1:k + 1])
        for i in range(n):
            res[i] = ans
            ans += code[i + k + 1] - code[i + 1]
        if flag:
            res.reverse()
        return res