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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s = 0
        node1, node2 = l1, l2
        res_head = res_tail = ListNode()
        while node1 or node2 or s:
            node = ListNode()
            if node1 and node2:
                s += (node1.val + node2.val)
                node1 = node1.next
                node2 = node2.next
            elif node1:
                s += node1.val
                node1 = node1.next
            elif node2:
                s += node2.val
                node2 = node2.next
            node.val = int(str(s)[-1])
            res_tail.next = node
            res_tail = res_tail.next
            s = int(str(s)[:-1]) if str(s)[:-1] else 0
        return res_head.next
