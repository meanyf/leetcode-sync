class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, item in enumerate(s):
            d[item] = i

        res =[]
        mx = l = 0
        for i, ch in enumerate(s):
            mx = max(mx, d[ch])
            if i == mx:
                res.append(i - l + 1)
                l = i + 1
        return res