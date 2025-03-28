class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for item in s:
            d[item] = d.get(item, 0) + 1
        
        lst = sorted(d.items(), key=lambda x: -x[1])
        res = ''
        for item in lst:
            res += item[0] * item[1]
        return res