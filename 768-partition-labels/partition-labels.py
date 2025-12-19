class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, item in enumerate(s):
            d[item] = i
        
        mx = -1
        res = []
        l = 0
        for i, ch in enumerate(s):
            mx = max(mx, d[ch])
            if i == mx:
                mx = -1
                res.append(i - l + 1)
                l = i + 1
        return res