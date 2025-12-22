from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
            g[src].append(dest)
        stack = ['JFK']
        res = []
        while stack:
            node = stack[-1]
            if g[node]:
                next_node = g[node].pop(0)
                stack.append(next_node)
            else:
                res.append(stack.pop())
        return res[::-1]
            