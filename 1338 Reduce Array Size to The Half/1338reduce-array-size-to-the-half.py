class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        d = {}
        for num in arr:
            d[num] = d.get(num, 0) + 1
        
        length = len(arr) // 2
        lst = sorted(d.items(), key=lambda x: -x[1])
        cnt = 0
        i = 0
        while i < len(arr) and cnt < length:
            cnt += lst[i][1]
            i += 1
        return i