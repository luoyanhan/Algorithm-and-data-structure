class Solution:
    def lengthLongestPath(self, input: str) -> int:
        li = input.split('\n')
        stack = list()
        pre_depth = 0
        res = 0
        for idx in range(len(li)):
            cur_part = li[idx]
            cur_depth = cur_part.count('\t')
            tmp_pre_depth = pre_depth
            while cur_depth <= tmp_pre_depth:
                if stack:
                    stack.pop()
                tmp_pre_depth -= 1
            stack.append(cur_part.replace('\t', ''))
            pre_depth = cur_depth
            if '.' in cur_part:
                res = max(res, sum([len(x) for x in stack]) + len(stack) - 1)
        return res



print(Solution().lengthLongestPath("a.txt"))




