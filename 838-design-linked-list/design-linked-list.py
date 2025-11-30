class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size: return -1
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.dummy.next = Node(val, next=self.dummy.next, prev=self.dummy)
        if self.size > 0: 
            self.dummy.next.next.prev = self.dummy.next
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = Node(val, prev=cur)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: 
            return 
        cur = self.dummy
        for _ in range(index):
            cur = cur.next
        cur.next = Node(val, next=cur.next, prev=cur)
        if cur.next.next is not None:
            cur.next.next.prev = cur.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size: 
            return 
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next
        cur.prev.next = cur.next
        if index != self.size - 1:
            cur.next.prev = cur.prev
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)