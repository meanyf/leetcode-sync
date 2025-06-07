# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        node = TreeNode()
        stack = [(root1, root2, node)]
        while stack:
            node1, node2, merged_node = stack.pop()
            if merged_node:
                merged_node.val = (node1.val if node1 else 0) + (node2.val if node2 else 0)
            if node1 or node2:
                if (node1 and node1.left) or (node2 and node2.left):
                    merged_node.left = TreeNode()
                if (node1 and node1.right) or (node2 and node2.right):
                    merged_node.right = TreeNode()
                stack.append((node1.right if node1 else None, node2.right if node2 else None, merged_node.right))
                stack.append((node1.left if node1 else None, node2.left if node2 else None, merged_node.left))
        return node