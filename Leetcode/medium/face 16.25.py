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
        self.mapper = dict()
        self.length = 0


    def get(self, key: int) -> int:
        if key not in self.mapper:
            return -1
        node = self.mapper[key]
        self.move_to_head(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.mapper:
            node = self.mapper[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            if self.length < self.capacity:
                self.length += 1
            else:
                self.del_tail()
            self.add_to_head(node)
            self.mapper[key] = node


    def del_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = None
        node.pre = None
        return node

    def del_tail(self):
        if self.length > 0:
            del self.mapper[self.tail.pre.key]
            self.tail.pre = self.tail.pre.pre
            self.tail.pre.next = self.tail

    def add_to_head(self, node):
        node.next = self.head.next
        node.next.pre = node
        self.head.next = node
        node.pre = self.head

    def move_to_head(self, node):
        node = self.del_node(node)
        self.add_to_head(node)


