class Solution:
    def validStrings(self, n: int) -> list[str]:
        result = []
            
        def b(current: list):
            if len(current) == n:
                result.append(list(current))
                return
            for i in range(2):
                if current and current[-1] == 0 and i == 0:
                    continue
                current.append(i)
                b(current)
                current.pop()
        b([])
        result = list([''.join(str(y) for y in x) for x in result])
        return result