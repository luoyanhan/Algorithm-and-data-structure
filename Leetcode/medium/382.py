# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import random
class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        cur = self.head
        idx = 0
        res = cur.val
        while cur:
            num = random.randint(0, idx)
            if num == idx:
                res = cur.val
            cur = cur.next
            idx += 1
        return res