#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        visiting = set()
        nodes = range(numCourses)
        g = defaultdict(list)
        for item, val in prerequisites:
            g[val].append(item)

        for start in nodes:
            if start in visited:
                continue
            stack = [(start, False)]
            while stack:
                node, expanded = stack.pop()

                if expanded:
                    visited.add(node)
                    visiting.remove(node)
                    res.append(node)
                    continue

                # if node in visiting:
                #     return False
                if node in visited:
                    continue

                visiting.add(node)
                stack.append((node, True))
                for nei in g[node]:
                    if nei in visiting:
                        return []
                    if nei in visited:
                        continue
                    stack.append((nei, False))

        return res[::-1]


# @lc code=end
