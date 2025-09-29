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
        d = dict()
        mx = -float('inf')

        while stack:
            node, visited = stack.pop()
            if not node: continue
            if visited:
                right = d.get(node.right, 0)
                left = d.get(node.left, 0)
                d[node] = max(node.val, node.val + right, node.val + left)
                mx = max(mx, node.val + right + left, d[node])
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return mx
