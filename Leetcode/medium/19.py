# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        interval = 0
        left = head
        right = head
        while right.next:
            if interval < n:
                interval += 1
            else:
                left = left.next
            right = right.next
        if interval < n:
           return head.next
        else:
            left.next = left.next.next
            return head
