# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        current = root
        res = []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                if node:
                    res.append(node.val)
                    current = node.right
        if len(res) == 1: return True
        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False
        return True