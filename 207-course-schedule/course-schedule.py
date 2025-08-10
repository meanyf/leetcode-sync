#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#


# @lc code=start
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
                    continue

                if node in visiting:
                    return False
                if node in visited:
                    continue

                visiting.add(node)
                stack.append((node, True))
                for nei in g[node]:
                    if nei in visiting:
                        return False
                    stack.append((nei, False))

        return True
        # visited = set()
        # visiting = set()
        # nodes = range(numCourses)
        # g = defaultdict(list)
        # for item, val in prerequisites:
        #     g[val].append(item)

        # def dfs(node):
        #     if node in visiting:
        #         return False
        #     if node in visited:
        #         return True

        #     visiting.add(node)
        #     for nei in g[node]:
        #         if not dfs(nei):
        #             return False

        #     visiting.discard(node)
        #     visited.add(node)
        #     return True

        # for node in nodes:
        #     if not dfs(node):
        #         return False
        # return True


# @lc code=end
