class Solution:
    def exclusiveTime(self, n: int, logs):
        res = [0] * n
        log0_li = logs[0].split(':')
        pre = int(log0_li[2])
        stack = [log0_li[0]]
        for i in range(1, len(logs)):
            log_li = logs[i].split(':')
            if log_li[1] == 'start':
                if stack:
                    res[int(stack[-1])] += int(log_li[2]) - pre
                pre = int(log_li[2])
                stack.append(log_li[0])
            else:
                top = int(stack.pop())
                res[top] += int(log_li[2]) - pre + 1
                pre = int(log_li[2]) + 1
        return res
