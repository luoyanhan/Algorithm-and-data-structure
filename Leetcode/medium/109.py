# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head):
        def getmiddle(left, right):
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        def inner(left, right):
            if left == right:
                return None
            middle = getmiddle(left, right)
            root = TreeNode(middle.val)
            root.left = inner(left, middle)
            root.right = inner(middle.next, right)
            return root
        return inner(head, None)


class Solution:
    def sortedListToBST(self, head):
        def get_length(left):
            node = left
            res = 0
            while node:
                res += 1
                node = node.next
            return res
        def inner(left, right):
            if left > right:
                return None
            mid = (left+right+1)//2
            root = TreeNode()
            root.left = inner(left, mid-1)
            nonlocal head
            root.val = head.val
            head = head.next
            root.right = inner(mid+1, right)
            return root
        length = get_length(head)
        return inner(0, length-1)