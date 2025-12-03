from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for src, dest in tickets:
            g[src].append(dest)
        for src in g:
            g[src].sort(reverse=True)
        stack = ['JFK']
        route = []
        while stack:
            src = stack[-1]
            if g[src]:
                next_city = g[src].pop()
                stack.append(next_city)
            else:
                route.append(stack.pop())
        return route[::-1]



        