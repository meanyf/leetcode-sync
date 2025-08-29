from collections import defaultdict
from itertools import combinations
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        by_y = defaultdict(list)
        for item in points:
            by_y[item[1]].append(item[0])

        d = defaultdict(set)

        for y, xs in by_y.items():
            xs.sort()
            for i in range(len(xs)):
                for j in range(i + 1, len(xs)):
                    ans = (xs[i], xs[j])   # sorted не нужен, т.к. xs уже отсортирован
                    d[ans].add(y)
        mn = float('inf')
        for key in d:
            dx = abs(key[0] - key[1])
            ans = float('inf')
            for item, p in combinations(d[key], 2):
                if item != p:
                    ans = min(ans, abs(item - p))
            mn = min(mn, ans*dx)
        return mn if mn < float('inf') else 0