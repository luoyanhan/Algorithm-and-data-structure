# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res = ListNode(0)
        res.next = head
        order_tail = head
        cur = head.next
        while cur:
            if cur.val < order_tail.val:
                pre = res
                while pre.next and pre.next.val < cur.val:
                    pre = pre.next
                tmp = pre.next
                pre.next = cur
                order_tail.next = cur.next
                cur.next = tmp
                cur = order_tail.next
            else:
                cur = cur.next
                order_tail = order_tail.next
        return res.next