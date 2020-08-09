# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head):
        preSum = dict()
        tmpSum = 0
        res = ListNode(0)
        res.next = head
        node = res
        while node:
            tmpSum += node.val
            if tmpSum not in preSum:
                preSum[tmpSum] = node
            else:
                tmpNode, s = preSum[tmpSum].next, tmpSum
                preSum[tmpSum].next = node.next
                while tmpNode != node:
                    s += tmpNode.val
                    del preSum[s]
                    tmpNode = tmpNode.next
            node = node.next
        return res.next

