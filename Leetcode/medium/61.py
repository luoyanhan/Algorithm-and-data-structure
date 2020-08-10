# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
        length = 1
        node = head
        while node.next:
            node = node.next
            length += 1
        last = node
        k %= length
        if not k:
            return head
        node = head
        for i in range(length-k-1):
            node = node.next
        res = node.next
        node.next = None
        last.next = head
        return res
