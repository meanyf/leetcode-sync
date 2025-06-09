# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        stack = [(root1, root2)]
        res1 = []
        res2 = []
        while stack:
            node1, node2 = stack.pop()
            if node1 and not node1.left and not node1.right:
                res1.append(node1.val)
            if node2 and not node2.left and not node2.right:
                res2.append(node2.val)
            if node1 or node2:
                stack.append((node1.right if node1 else None, node2.right if node2 else None))
                stack.append((node1.left if node1 else None, node2.left if node2 else None))
        
        return res1 == res2