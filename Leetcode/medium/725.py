# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root, k):
        tmp = root
        length = 0
        while tmp:
            length += 1
            tmp = tmp.next
        base = length // k
        yushu = length % k
        num_li = [base] * k
        def get(num, root):
            if num == 0:
                return None, None
            pre = root
            while num > 1:
                pre = pre.next
                num -= 1
            remain = pre.next
            pre.next = None
            return root, remain
        res = list()
        remain = root
        for num in num_li:
            if yushu:
                yushu -= 1
                num += 1
            child, remain = get(num, remain)
            res.append(child)
        return res



