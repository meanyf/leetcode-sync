# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        right = True
        while q:
            lst = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    lst.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if lst:
                if right:
                    res.append(lst)
                else:
                    res.append(lst[::-1])
            right = not right
        return res