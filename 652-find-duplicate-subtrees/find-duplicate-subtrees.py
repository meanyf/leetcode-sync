# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d = {}
        cnt = {}
        if not root:
            return []
        stack = [(root, False)]
        res = []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    left = d.get(node.left, None)
                    right = d.get(node.right, None)
                    val = (node.val, left, right)
                    d[node] = val
                    cnt[val] = cnt.get(val, 0) + 1
                    if cnt[val] == 2:
                        res.append(node)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res