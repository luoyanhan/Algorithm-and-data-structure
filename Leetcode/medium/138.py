
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return head
        idx = head
        while idx:
            new_node = Node(idx.val, None, None)
            new_node.next = idx.next
            idx.next = new_node
            idx = new_node.next

        idx = head
        while idx:
            idx.next.random = idx.random.next if idx.random else None
            idx = idx.next.next

        new_list = head.next
        res = new_list
        old_list = head
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        return res


