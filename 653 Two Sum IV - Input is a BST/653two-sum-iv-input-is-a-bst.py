# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        lst = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)
        dfs(root)
        l = 0
        r = len(lst) - 1
        while l < r:
            if lst[l] + lst[r] == k:
                return True
            elif lst[l] + lst[r] > k:
                r -= 1
            else:
                l += 1
        return False


        # d = {}
        # def dfs(node):
        #     if not node:
        #         return False
        #     if k - node.val in d:
        #         return True
        #     d[node.val] = True
        #     return dfs(node.left) or dfs(node.right)
        # return dfs(root)
        