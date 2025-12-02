class Node:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if len(self.d) == 0:
            return -1
        if key not in self.d:
            return -1
        node = self.d[key]
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev

        nxt, prev = self.left.next, self.left
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.get(key)
            return
        if len(self.d) == self.capacity:
            del_node = self.right.prev
            nxt, prev = del_node.next, del_node.prev
            prev.next = nxt
            nxt.prev = prev
            self.d.pop(del_node.key, None)

            node, nxt, prev = Node(val=value, key=key), self.left.next, self.left
            nxt.prev = node
            prev.next = node
            node.prev = prev
            node.next = nxt
            self.d[key] = node
        else:
            node, nxt, prev = Node(val=value, key=key), self.left.next, self.left
            nxt.prev = node
            prev.next = node
            node.prev = prev
            node.next = nxt
            self.d[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)