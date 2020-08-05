# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        res = ListNode(0)
        res.next = head
        pre = res
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if pre.next == head:
                pre = pre.next
            else:
                pre.next = head.next
            head = head.next
        return res.next




