# Definition for a binary tree node.
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
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        b = TreeNode() 
        
        def dfs(node, dummy):
            if not node:
                return dummy  

            dummy = dfs(node.left, dummy)
            dummy.right = TreeNode(node.val)
            dummy = dummy.right  
            return dfs(node.right, dummy) 

        dfs(root, b)
        return b.right