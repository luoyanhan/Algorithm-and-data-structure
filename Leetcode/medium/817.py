# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        cnt = 0
        G = set(G)
        while head:
            if head.val in G and getattr(head.next, 'val', None) not in G:
                cnt += 1
            head = head.next
        return cnt
