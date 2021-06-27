class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail_of_2 = list2
        while tail_of_2.next:
            tail_of_2 = tail_of_2.next
        left = None
        right = list1
        for i in range(b+1):
            if i == a-1:
                left = right
            right = right.next

        left.next = list2
        list2.pre = left
        tail_of_2.next = right
        right.pre = tail_of_2
        return list1