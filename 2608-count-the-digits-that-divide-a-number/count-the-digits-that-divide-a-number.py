class Solution:
    def countDigits(self, num: int) -> int:
        lst = map(int, str(num))
        return sum(num % item == 0 for item in lst)