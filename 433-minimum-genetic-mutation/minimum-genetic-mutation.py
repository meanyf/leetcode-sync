from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set([startGene])
        q = deque()
        q.append((startGene, 0))
        while q:
            cur, dist = q.popleft()
            if cur == endGene:
                print(cur)
                return dist
            for item in bank:
                if item in visited:
                    continue
                differ_by_one = lambda cur, item: len(cur) == len(item) and sum(a != b for a, b in zip(cur, item)) == 1
                if differ_by_one(cur, item):
                    q.append((item, dist + 1))
                    visited.add(item)
        return -1

