class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size: return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, next=self.head)
        if self.size == 0:
            self.tail = self.head
        else:
            self.head.next.prev = self.head
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val, prev=self.tail)
            self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return None
        if self.size == 0:
            self.head = self.tail = Node(val)
        elif index == 0:
            self.head = Node(val, self.head)
            self.head.next.prev = self.head
        elif self.size == index:
            self.tail.next = Node(val, prev=self.tail)
            self.tail = self.tail.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = Node(val, next=cur.next, prev=cur)
            cur.next.next.prev = cur.next
        self.size += 1
        


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size: return None
        if self.size == 1: 
            self.head = self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
            cur.next.prev = cur
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)