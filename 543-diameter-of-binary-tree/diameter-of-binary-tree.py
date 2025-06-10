# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        values = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                if not node.left and not node.right:
                    values[node] = 0
                else:
                    left = 1 if node.left else 0
                    right = 1 if node.right else 0
                    res = max(res, values.get(node.left, 0) + left + values.get(node.right, 0) + right)
                    values[node] = max(values.get(node.left, 0) + 1, values.get(node.right, 0) + 1) 
                res = max(res, values[node])
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        print(values.values())
        return res