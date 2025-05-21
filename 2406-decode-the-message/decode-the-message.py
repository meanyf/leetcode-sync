class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        lst = 'abcdefghijklmnopqrstuvwxyz'
        key = key.replace(' ', '')
        d_set = {}
        for item in key:
            d_set[item] = True
        d = {}
        idx = 0
        for item in list(d_set.keys()):
            d[item] = lst[idx]
            idx += 1
        res = []
        for item in message:
            if item == ' ':
                res.append(item)
            else:
                res.append(d[item])
        return ''.join(res)