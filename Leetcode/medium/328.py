# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        odd_tail = head
        even_head = head.next
        even_tail = even_head
        is_odd = True
        node = head.next.next
        while node:
            if is_odd:
                is_odd = False
                odd_tail.next = node
                odd_tail = odd_tail.next
            else:
                is_odd = True
                even_tail.next = node
                even_tail = even_tail.next
            node = node.next
        even_tail.next = None
        odd_tail.next = even_head
        return head
