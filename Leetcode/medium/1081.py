from collections import defaultdict
class Solution:
    def smallestSubsequence(self, s):
        cnt = defaultdict(int)
        visited = set()
        for each in s:
            cnt[each] += 1
        stack = list()
        for each in s:
            if each not in visited:
                while stack and stack[-1] > each and cnt[stack[-1]] > 0:
                    visited.remove(stack[-1])
                    stack.pop()
                stack.append(each)
                visited.add(each)
            cnt[each] -= 1
        return ''.join(stack)