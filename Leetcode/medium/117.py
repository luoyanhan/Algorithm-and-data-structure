
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return root
        queue = [root, None]
        while queue:
            top = queue.pop(0)
            if top:
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
                top.next = queue[0]
            else:
                if queue:
                    queue.append(None)
        return root


class Solution:
    def connect(self, root):
        if not root:
            return root
        dummy = Node()
        pre = dummy
        cur = root
        while cur:
            if cur.left:
                pre.next = cur.left
                pre = pre.next
            if cur.right:
                pre.next = cur.right
                pre = pre.next
            cur = cur.next
            if not cur:
                cur = dummy.next
                dummy.next = None
                pre = dummy
        return root


class Solution:
    def connect(self, root):
        if not root:
            return root
        def inner(child, pre, leftmost):
            if child:
                if pre:
                    pre.next = child
                else:
                    leftmost = child
                pre = child
            return pre, leftmost
        leftmost = root
        while leftmost:
            pre, cur = None, leftmost
            leftmost = None
            while cur:
                pre, leftmost = inner(cur.left, pre, leftmost)
                pre, leftmost = inner(cur.right, pre, leftmost)
                cur = cur.next
        return root


