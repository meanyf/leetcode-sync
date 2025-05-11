# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = dict()
        mx = 0
        def dfs(node):
            nonlocal mx
            if not node:
                return
            dfs(node.left)
            d[node.val] = d.get(node.val, 0) + 1
            mx = max(d[node.val], mx)
            dfs(node.right)
        dfs(root)
        res = []
        for k in d:
            if d[k] == mx:
                res.append(k)
        return res

        