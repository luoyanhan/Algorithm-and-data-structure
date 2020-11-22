# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#归并方法，递归
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next  #前后要差一位，否则会死循环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None #要记得断开
        left = self.sortList(head)
        right = self.sortList(mid)
        res = ListNode()
        h = res
        while left and right:
            if left.val <= right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next

#归并，非递归
class Solution:
    def sortList(self, head):
        h = head
        length = 0
        while h:
            h = h.next
            length += 1
        step = 1
        res = ListNode()
        res.next = head
        while step < length:
            pre = res
            h = res.next
            while h:
                left = h
                cnt = step
                while cnt > 0 and h:
                    h = h.next
                    cnt -= 1
                if cnt > 0:
                    break
                right = h
                cnt = step
                while cnt > 0 and h:
                    cnt -= 1
                    h = h.next
                len_left = step
                len_right = step - cnt
                while len_left > 0 and len_right > 0:
                    if left.val <= right.val:
                        pre.next = left
                        left = left.next
                        len_left -= 1
                    else:
                        pre.next = right
                        right = right.next
                        len_right -= 1
                    pre = pre.next
                if len_left:
                    pre.next = left
                    while len_left > 0:
                        len_left -= 1
                        pre = pre.next
                elif len_right:
                    pre.next = right
                    while len_right > 0:
                        len_right -= 1
                        pre = pre.next
                pre.next = h    #记得重回正轨
            step *= 2
        return res.next

