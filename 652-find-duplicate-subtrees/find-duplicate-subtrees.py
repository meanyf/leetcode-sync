#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    left = d.get(node.left, "#")
                    right = d.get(node.right, "#")
                    serial = f'{node.val},{left},{right}'
                    d[node] = serial
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        g = {}
        res = []
        for key, val in d.items():
            g[val] = g.get(val, 0) + 1
            if g[val] == 2:
                res.append(key)
        return res

# @lc code=end
