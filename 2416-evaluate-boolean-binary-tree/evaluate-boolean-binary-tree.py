# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if node.val == 2:
                        node.val = (node.left.val or node.right.val)
                    if node.val == 3:
                        node.val = (node.left.val and node.right.val)
                else:
                    stack.append((node, True))
                    if node.right:
                        stack.append((node.right, False))
                    if node.left:
                        stack.append((node.left, False))

        return bool(root.val)