# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            left = right = 0
            if node.val > low: 
                left = dfs(node.left)
            if node.val < high: 
                right = dfs(node.right)
            res = node.val if low <= node.val <= high else 0
            res += left + right
            return res

        return dfs(root)