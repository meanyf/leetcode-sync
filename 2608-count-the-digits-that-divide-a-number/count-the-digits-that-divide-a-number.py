class Solution:
    def countDigits(self, num: int) -> int:
        lst = map(int, str(num))
        cnt = 0
        for item in lst:
            if num % item == 0:
                cnt += 1
        return cnt