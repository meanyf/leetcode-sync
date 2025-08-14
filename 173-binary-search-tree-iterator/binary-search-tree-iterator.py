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

    def next(self) -> int:
        if self.stack and not self.cur:
            node = self.stack.pop()
            self.cur = node.right
            return node.val
        while self.cur:
            if self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
        node = self.stack.pop()
        self.cur = node.right
        return node.val
        # return self.res.popleft()
    def hasNext(self) -> bool:
        return True if self.cur or self.stack else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()