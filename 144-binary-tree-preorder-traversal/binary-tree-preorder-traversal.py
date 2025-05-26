# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            stack = [root]
            if not root:
                return []
            res = []
            while stack:
                node = stack.pop()
                if node:
                    res.append(node.val)
                    stack.append(node.right)
                    stack.append(node.left)
            return res
            # res = []
            # def dfs(node):
            #     if not node:
            #         return 
            #     res.append(node.val)
            #     dfs(node.left)
            #     dfs(node.right)
                
            # dfs(root)
            # return res