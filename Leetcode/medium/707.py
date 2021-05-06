class Node:
    def __init__(self):
        self.val = None
        self.next = None
        self.pre = None

class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head


    def get(self, index: int) -> int:
        if not self.length > index >= 0 and self.length > 0:
            return -1
        node = self.head
        for i in range(index+1):
            node = node.next
        return node.val



    def addAtHead(self, val: int) -> None:
        node = Node()
        node.val = val
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
        node.next.pre = node
        self.length += 1


    def addAtTail(self, val: int) -> None:
        node = Node()
        node.val = val
        node.pre = self.tail.pre
        node.pre.next = node
        node.next = self.tail
        self.tail.pre = node
        self.length += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            self.addAtTail(val)
        elif index <= 0:
            self.addAtHead(val)
        elif self.length > index > 0:
            node = Node()
            node.val = val
            tar = self.head
            for i in range(index+1):
                tar = tar.next
            node.pre = tar.pre
            tar.pre = node
            node.pre.next = node
            node.next = tar
            self.length += 1



    def deleteAtIndex(self, index: int) -> None:
        if self.length > index >= 0 and self.length > 0:
            tar = self.head
            for i in range(index + 1):
                tar = tar.next
            tar.pre.next = tar.next
            tar.next.pre = tar.pre
            tar.pre = None
            tar.next = None
            self.length -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)