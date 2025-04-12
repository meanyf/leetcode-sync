class Solution:
    def maximum69Number (self, num: int) -> int:
        lst = [int(d) for d in str(num)]
        for idx in range(len(lst)):
            if lst[idx] == 6:
                lst[idx] = 9
                return int(''.join(str(x) for x in lst))
        return int(''.join(str(x) for x in lst))
