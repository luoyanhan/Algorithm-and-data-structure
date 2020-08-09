# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        li = list()
        node = head
        cnt = 0
        while node:
            li.append(node)
            node = node.next
            cnt += 1
        mid = (cnt-1)//2
        node = head
        while mid > 0:
            mid -= 1
            top = li.pop()
            tmp = node.next
            node.next = top
            top.next = tmp
            node = top.next
        li.pop().next = None
        return head
