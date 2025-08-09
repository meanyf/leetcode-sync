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

        def dfs(node):
            visited.add(node)
            visiting.add(node)
            for nei in g[node]:
                if nei in visiting:
                    return False
                if nei not in visited:
                    if not dfs(nei):
                        return False
            visiting.discard(node)
            return True
        
        for node in nodes:
            if node not in visited:
                if not dfs(node): 
                    return False
        return True


# @lc code=end
