class Node:
    def __init__(self):
        self.pre = None
        self.next = None
        self.value = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node()
        self.cur = Node()
        self.cur.value = homepage
        self.cur.pre = self.head
        self.head.next = self.cur
        self.tail = Node()
        self.tail.pre = self.cur
        self.cur.next = self.tail
        self.to_head = 1
        self.to_tail = 1

    def visit(self, url: str) -> None:
        node = Node()
        node.value = url
        node.pre = self.cur
        self.cur.next = node
        node.next = self.tail
        self.tail.pre = node
        self.cur = node
        self.to_head += 1
        self.to_tail = 1


    def back(self, steps: int) -> str:
        if steps >= self.to_head:
            self.cur = self.head.next
            self.to_tail = self.to_head + self.to_tail - 1
            self.to_head = 1
        else:
            for i in range(steps):
                self.cur = self.cur.pre
                self.to_head -= 1
                self.to_tail += 1
        return self.cur.value



    def forward(self, steps: int) -> str:
        if steps >= self.to_tail:
            self.cur = self.tail.pre
            self.to_head = self.to_head + self.to_tail - 1
            self.to_tail = 1
        else:
            for i in range(steps):
                self.cur = self.cur.next
                self.to_head += 1
                self.to_tail -= 1
        return self.cur.value