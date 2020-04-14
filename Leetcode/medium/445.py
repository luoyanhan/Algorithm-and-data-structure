class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def changetoStack(node):
            res = []
            while node:
                res.append(node.val)
                node = node.next
            return res
        L1 = changetoStack(l1)
        L2 = changetoStack(l2)
        length = min([len(L1), len(L2)])
        result = list()
        over = 0
        for i in range(length):
            num = over + L1.pop() + L2.pop()
            over = int(num/10)
            result = [num % 10] + result
        if L1:
            for i in range(len(L1)):
                num = over + L1.pop()
                over = int(num / 10)
                result = [num % 10] + result
        elif L2:
            for i in range(len(L2)):
                num = over + L2.pop()
                over = int(num / 10)
                result = [num % 10] + result
        if over > 0:
            result = [over] + result
        result_node = ListNode(result[0])
        start = result_node
        for i in range(1, len(result)):
            result_node.next = ListNode(result[i])
            result_node = result_node.next
        return start





