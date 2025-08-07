#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        g = {}
        for i, item in enumerate(rooms):
            g.setdefault(i, []).extend(item)
        print(g)
        visited = set()
        stack = [0]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for item in g.get(node, []):
                stack.append(item)
        print(visited)
        return len(visited) == len(rooms)
# @lc code=end

