# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        a = 0
        def dfs(node, num = ''):
            nonlocal a
            if not node:
                return
            if not node.left and not node.right:
                a += int(num + str(node.val), 2)
                print(num)
                return 
            dfs(node.left, num + str(node.val))
            dfs(node.right, num + str(node.val))
            
        dfs(root)
        return a