# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        def dfs1(node):
            if not node:
                res1.append(None)
                return 
            res1.append(node.val)
            dfs1(node.left)
            dfs1(node.right)
        def dfs2(node):
            if not node:
                res2.append(None)
                return 
            res2.append(node.val)
            dfs2(node.right)
            dfs2(node.left)
        dfs1(root.left)
        dfs2(root.right)
        print(res1, res2)
        return res1 == res2