# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        node = head
        visited = set()
        while node:
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None


class Solution:
    def detectCycle(self, head):
        node1 = head
        node2 = head
        while True:
            if not node2 or not node2.next:
                return None
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                break
        ptr1 = node1
        ptr2 = head
        while True:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next



