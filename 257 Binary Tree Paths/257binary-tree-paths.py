# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node, num = ''):
            if num:
                num = str(num) + '->'
            if not node:
                return 
            if not node.left and not node.right:
                res.append(num + str(node.val))
            dfs(node.left, str(num) + str(node.val))
            dfs(node.right, str(num) + str(node.val))
        dfs(root)
        return res