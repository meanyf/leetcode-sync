"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        lst = []
        def dfs(node):
            if not node:
                return
            for ch in node.children:
                dfs(ch)
            lst.append(node.val)  
        dfs(root)
        return lst