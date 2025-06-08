# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, '')]
        res = 0
        while stack:
            node, path = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += int(path + str(node.val), 2)
                stack.append((node.right, path + str(node.val)))
                stack.append((node.left, path + str(node.val)))
        return res
        # a = 0
        # def dfs(node, num = ''):
        #     nonlocal a
        #     if not node:
        #         a += int(num, 2)
        #         return
        #     dfs(node.left, num + str(node.val))
        #     dfs(node.right, num + str(node.val))
            
        # dfs(root)
        # return a // 2