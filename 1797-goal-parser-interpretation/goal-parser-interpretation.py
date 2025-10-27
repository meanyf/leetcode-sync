class Solution:
    def interpret(self, command: str) -> str:
        res = []
        d = {'G': 'G', '()': 'o', '(al)': 'al'}
        cur = ''
        for item in command:
            cur += item
            if cur in d:
                res.append(d[cur])
                cur = ''
        return ''.join(res)
