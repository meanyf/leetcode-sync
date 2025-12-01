class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size: return -1
        cur = self.left.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: 
            return 
        cur = self.left
        for _ in range(index):
            cur = cur.next
        cur.next = Node(val, next=cur.next, prev=cur)
        cur.next.next.prev = cur.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size: 
            return 
        cur = self.left.next
        for _ in range(index):
            cur = cur.next
        cur.prev.next = cur.next
        cur.next.prev = cur.prev 
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)