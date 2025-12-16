# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, False)]
        res = -math.inf
        d = {}
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    left = d.get(node.left, 0)
                    right = d.get(node.right, 0)
                    d[node] = max(node.val, node.val + left, node.val + right)
                    res = max(d[node], res, node.val + left + right)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res