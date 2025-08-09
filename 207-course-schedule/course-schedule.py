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
        nodes = set()
        g = defaultdict(list)
        for item, val in prerequisites:
            g[val].append(item)
            nodes.add(item)
            nodes.add(val)

        stack = []
        x = True
        def dfs(node):
            nonlocal x
            if x == False:
                return
            visited.add(node)
            visiting.add(node)
            for nei in g[node]:
                if nei in visiting:
                    x = False
                    return
                if nei not in visited:
                    dfs(nei)
            visiting.discard(node)
            stack.append(node)

        for node in nodes:
            if node in visiting: return False
            if node not in visited:
                dfs(node)

        print(stack[::-1])
        return x


# @lc code=end
