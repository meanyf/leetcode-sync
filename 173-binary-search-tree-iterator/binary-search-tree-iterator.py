# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self.cur = root
        self.res = deque([])
        while self.cur or self.stack:
            if self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            else:
                node = self.stack.pop()
                self.res.append(node.val)
                self.cur = node.right

    def next(self) -> int:
        return self.res.popleft()
    def hasNext(self) -> bool:
        return True if self.res else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()