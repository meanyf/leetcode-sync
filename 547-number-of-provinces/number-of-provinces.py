#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = {i: [] for i in range(len(isConnected))}
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
        if not graph: return 0

        # for key, val in graph.items():
        #     print(f"{key}: {val}")

        visited = set()
        cnt = 0

        def dfs_stack(start, graph, visited):
            stack = [start]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                for neighbor in graph[node]:
                    stack.append(neighbor)
        
        for node in graph:
            if node not in visited:
                cnt += 1
                dfs_stack(node, graph, visited)
        return cnt


# @lc code=end
