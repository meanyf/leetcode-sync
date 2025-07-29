class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for item in address:
            if item != '.':
                res.append(item)
            else:
                res.append('[.]')
        return ''.join(res)
        # return address.replace('.', '[.]')