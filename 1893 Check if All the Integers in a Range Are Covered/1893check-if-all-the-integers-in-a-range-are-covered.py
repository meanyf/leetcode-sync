class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        lst = [0] * 51
        for start, end in ranges:
            lst[start] += 1
            if end + 1 < len(lst):  
                lst[end + 1] -= 1
        prefix = [0] * (len(lst) + 1)
        for i in range(1, len(lst) + 1):
            prefix[i] = prefix[i - 1] + lst[i - 1]
        print(lst)
        print(prefix)
        for i in range(left, right + 1):
            if prefix[i + 1] <= 0:
                return False
        return True