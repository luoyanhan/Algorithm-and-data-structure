
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
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

