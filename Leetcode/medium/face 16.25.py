class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node('head', 0)
        self.tail = Node('tail', 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0
        self.mapper = dict()


    def get(self, key: int) -> int:
        if key in self.mapper:
            node = self.mapper[key]
            self.move_to_head(node)
            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.mapper:
            node = self.mapper[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.mapper[key] = node
            self.add_to_head(node)
            self.length += 1
            if self.length > self.capacity:
                del self.mapper[self.tail.pre.key]
                self.del_node(self.tail.pre)
                self.length -= 1


    def move_to_head(self, node):
        self.del_node(node)
        self.add_to_head(node)

    def del_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.pre = None

    def add_to_head(self, node):
        node.next = self.head.next
        node.pre = self.head
        node.next.pre = node
        self.head.next = node



