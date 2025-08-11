#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import deque, defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        tickets.sort()
        g = defaultdict(deque)
        for src, dest in tickets:
            g[src].append(dest)
        stack = ["JFK"]
        res = []
        while stack:
            while g[stack[-1]]:
                stack.append(g[stack[-1]].popleft())
            res.append(stack.pop())
        return res[::-1]


# @lc code=end
