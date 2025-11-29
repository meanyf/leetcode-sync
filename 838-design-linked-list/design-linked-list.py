class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        for _ in range(index):
            cur = cur.next if cur else None
        return cur.val if cur else -1

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        if self.tail is None:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head:
            if index > 0: return None
            self.head = self.tail = Node(val)
            return
        dummy = Node(0, self.head)
        cur = dummy
        for _ in range(index):
            cur = cur.next if cur else None
        
        if cur is None: return None
        if cur.next is None:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            return None

        nxt = cur.next
        cur.next = Node(val)
        cur.next.next = nxt 
        self.head = dummy.next


    def deleteAtIndex(self, index: int) -> None:
        if not self.head: return None
        dummy = Node(0, self.head)
        cur = dummy
        for _ in range(index):
            cur = cur.next if cur else None
        if cur is None: return None
        if cur.next is None: return None
        if cur.next.next is None:
            self.tail = cur

        cur.next = cur.next.next
        self.head = dummy.next
        if not self.tail:
            self.tail = self.head
        ...


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)