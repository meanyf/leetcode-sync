class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res = s.split(' ')
        if len(pattern) != len(res): return False
        d = {}
        i = 0
        used = set()
        for item in pattern:
            if item in d:
                if d[item] != res[i]:
                    return False
            else:
                if res[i] in used:
                    return False
                used.add(res[i])
                d[item] = res[i]
            i += 1
        return True