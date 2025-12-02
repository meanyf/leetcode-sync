class Node:
    def __init__(self, val=0, key=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left
        self.d = {}
        self.capacity = capacity

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.left, self.left.next 
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.remove(self.d[key])
        self.insert(self.d[key])
        return self.d[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.get(key)
            return
        if len(self.d) == self.capacity:
            node = self.right.prev
            self.remove(node)
            self.d.pop(node.key, None)

        node = Node(val=value, key=key)
        self.insert(node)
        self.d[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)