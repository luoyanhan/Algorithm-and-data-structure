# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:  # write by myself
    def reverseBetween(self, head, m, n):
        res = ListNode(0)
        res.next = head
        rev = ListNode(0)
        pre_m = res
        cnt = 1
        while pre_m.next and cnt != m:
            pre_m = pre_m.next
            cnt += 1
        rev.next = pre_m.next
        idx = rev.next
        while idx.next and cnt < n:
            cnt += 1
            second = idx.next
            idx.next = second.next
            second.next = rev.next
            rev.next = second
        pre_m.next = rev.next
        return res.next




class Solution:
    def reverseBetween(self, head, m, n):
        pre, cur = None, head
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        tail = cur
        pre_m = pre
        while n > 0:
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third
            n -= 1
        if pre_m:
            pre_m.next = pre
        else:
            head = pre
        tail.next = cur
        return head


