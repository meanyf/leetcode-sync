class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        i = 1
        for item in range(1, n):
            print(start + 2 * i)
            res = res ^ (start + 2 * i)
            i += 1
        return res