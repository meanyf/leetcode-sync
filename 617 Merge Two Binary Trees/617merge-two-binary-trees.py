# Definition for a binary tree node.
try:
    TreeNode
except NameError:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return
            node = TreeNode()
            node.val += (node1.val if node1 else 0) + (node2.val if node2 else 0)
            node.left = dfs(node1.left if node1 else 0, node2.left if node2 else 0)
            node.right = dfs(node1.right if node1 else 0, node2.right if node2 else 0)
            return node
        return dfs(root1, root2)
            
