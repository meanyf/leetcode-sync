class Solution:
    def countPoints(self, rings: str) -> int:
        d = {}
        for s in rings:
            if s.isdigit():
                d[s] = set()
        for i in range(1, len(rings)):
            if rings[i] in d:
                d[rings[i]].add(rings[i - 1])
        cnt = 0
        for k in d:
            if len(d[k]) == 3:
                cnt += 1
        return cnt
        