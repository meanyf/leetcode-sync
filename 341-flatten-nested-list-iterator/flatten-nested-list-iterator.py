# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):    
        self.stack = deque(nestedList)
        self.res = []
        self.i = 0
        k = 0
        while self.stack:
            item = self.stack.popleft()
            if isinstance(item, int):
                self.res.append(item)
                continue
            if isinstance(item, list):
                # print('list', k, item)
                self.stack.extendleft(item[::-1])
                continue
            if isinstance(item.getInteger(), int):
                self.stack.appendleft(item.getInteger())
            if item.getList():
                # print(k, item)
                self.stack.appendleft(item.getList())
            k += 1
        print('fewfwewe')
        print(self.res)
    def next(self) -> int:
        return self.res[self.i - 1]
    
    def hasNext(self) -> bool:
        self.i += 1
        return self.i <= len(self.res)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())