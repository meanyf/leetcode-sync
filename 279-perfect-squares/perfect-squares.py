from math import sqrt
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        q = deque()
        q.append((n, 0))
        visited = set([n])
        while q:
            cur, dist = q.popleft()
            if cur == 0:
                return dist
            for i in range(1, int(sqrt(cur)) + 1):
                nxt = cur - i*i
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, dist + 1))
        
