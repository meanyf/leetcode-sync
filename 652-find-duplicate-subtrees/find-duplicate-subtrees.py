# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d = {}
        d2 = {}
        if not root:
            return []
        stack = [(root, False)]
        res = []
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    left_ser = d.get(node.left, 'None')
                    right_ser = d.get(node.right, 'None')
                    val = (left_ser, node.val, right_ser)
                    d[node] = val
                    d2[val] = d2.get(val, 0) + 1
                    if d2[val] == 2:
                        res.append(node)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res