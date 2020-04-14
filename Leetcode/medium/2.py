# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ans = ListNode(0)
        curNode = ans
        while l1 or l2 or carry:
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curNode.next = ListNode(cur)
            curNode = curNode.next
        return ans.next
