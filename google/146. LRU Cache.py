class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {} # {key: node}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    # O(1) O(1)
    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]
        self._remove(node)
        del self.lookup[key]
        self.put(node.key, node.value)
        return node.value

    # O(1) O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self._remove(self.lookup[key])

        node = Node(key, value)
        self.lookup[key] = node

        if len(self.lookup) > self.capacity:
            tail = self.tail.pre
            self._remove(tail)
            del self.lookup[tail.key]

        head = self.head.next
        node.pre = self.head
        node.next = head
        head.pre = node
        self.head.next = node

    # O(1)
    def _remove(self, node):
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)