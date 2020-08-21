class Node:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0, 'head')
        self.tail = Node(0, 'tail')
        self.head.next = self.tail
        self.tail.pre = self.head
        self.d = dict()
        self.length = 0
        self.cap = capacity

    def movehead(self, key):
        node = self.d[key]
        if node.pre != self.head:
            pre = node.pre
            pre.next = node.next
            node.next.pre = pre
            tmp = self.head.next
            node.pre = self.head
            self.head.next = node
            node.next = tmp
            tmp.pre = node

    def get(self, key: int) -> int:
        if key in self.d:
            self.movehead(key)
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.d[key].key = key
            self.movehead(key)
        elif self.length == self.cap:
            node = Node(value, key)
            tail_node = self.tail.pre
            self.tail.pre = tail_node.pre
            tail_node.pre.next = self.tail
            del self.d[tail_node.key]
            tmp = self.head.next
            node.next = tmp
            tmp.pre = node
            node.pre = self.head
            self.head.next = node
            self.d[key] = node
        else:
            node = Node(value, key)
            tmp = self.head.next
            node.next = tmp
            tmp.pre = node
            node.pre = self.head
            self.head.next = node
            self.d[key] = node
            self.length += 1


