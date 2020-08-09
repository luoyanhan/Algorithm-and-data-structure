# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head):
        ans = list()
        stack = list()
        node = head
        idx = 0
        while node:
            while stack and stack[-1][0].val < node.val:
                top = stack.pop()
                ans[top[1]] = node.val
            stack.append((node, idx))
            ans.append(0)
            idx += 1
            node = node.next
        return ans