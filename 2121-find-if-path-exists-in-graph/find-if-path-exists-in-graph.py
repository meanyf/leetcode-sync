#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#


# @lc code=start
class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = {}
        for item, val in edges:
            graph.setdefault(item, []).append(val)
            graph.setdefault(val, []).append(item)
        stack = [source]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for item in graph.get(node, []):
                stack.append(item)
        return destination in visited


# @lc code=end
