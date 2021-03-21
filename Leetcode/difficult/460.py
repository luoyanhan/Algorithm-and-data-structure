from collections import defaultdict
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.fre = 0
        self.pre = None
        self.next = None

    def insert(self, pre, next):
        pre.next = self
        next.pre = self
        self.pre = pre
        self.next = next

def create_list():
    head = Node('key', 0)
    tail = Node('tail', 0)
    head.next = tail
    tail.pre = head
    return (head, tail)

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapper_node = dict()
        self.mapper_fre = defaultdict(create_list)
        self.cnt = 0
        self.min_fre = 0

    def del_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = None

    def increase(self, node):
        fre = node.fre
        node.fre += 1
        head, tail = self.mapper_fre[node.fre]
        node.insert(head, head.next)
        if node.fre == 1:
            self.min_fre = 1
        elif fre == self.min_fre:
            head, tail = self.mapper_fre[fre]
            if head.next == tail:
                self.min_fre += 1


    def get(self, key: int) -> int:
        if key not in self.mapper_node:
            return -1
        node = self.mapper_node[key]
        self.del_node(node)
        self.increase(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if self.capacity > 0:
            if key in self.mapper_node:
                node = self.mapper_node[key]
                self.del_node(node)
                node.value = value
                self.increase(node)
            else:
                if self.cnt >= self.capacity:
                    head, tail = self.mapper_fre[self.min_fre]
                    del self.mapper_node[tail.pre.key]
                    self.del_node(tail.pre)
                    self.cnt -= 1
                node = Node(key, value)
                self.increase(node)
                self.mapper_node[key] = node
                self.cnt += 1




