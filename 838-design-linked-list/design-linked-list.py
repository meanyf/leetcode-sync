class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
        self.head = Node(val, self.head)
        if self.size == 0:
            self.tail = self.head
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        if index > self.size: return None
        if self.size == 0:
            self.head = self.tail = Node(val)
        elif index == 0:
            self.head = Node(val, self.head)
        elif self.size == index:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        else:
            for _ in range(index - 1):
                cur = cur.next
            cur.next = Node(val, cur.next)
        self.size += 1
        


    def deleteAtIndex(self, index: int) -> None:
        if self.size == 0 or index >= self.size:
            return None
        dummy = Node(0, self.head)
        cur = dummy
        for _ in range(index):
            cur = cur.next if cur else None
        if cur.next.next is None:
            self.tail = None if cur is dummy else cur
            
        cur.next = cur.next.next
        self.head = dummy.next
        if not self.tail:
            self.tail = self.head
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)