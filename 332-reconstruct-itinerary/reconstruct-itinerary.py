from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for src, dest in tickets:
            g[src].append(dest)
        for src in g:
            g[src].sort(reverse=True)
        stack = ['JFK']
        res = []
        while stack:
            node = stack[-1]
            if g[node]:
                next_node = g[node].pop()
                stack.append(next_node)
            else:
                res.append(stack.pop())
        return res[::-1]
            