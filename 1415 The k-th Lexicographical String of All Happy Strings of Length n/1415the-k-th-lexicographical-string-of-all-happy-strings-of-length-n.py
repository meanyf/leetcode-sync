class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        s = 'abc'
        def m(current: list):
            if len(result) >= k:
                return
            if len(current) == n:
                result.append(list(current))
                return
            for ch in s:
                if current and current[-1] == ch:
                    continue
                current.append(ch)
                m(current)
                current.pop()
        m([])
        return '' if k > len(result) else ''.join(sorted(result)[k - 1])