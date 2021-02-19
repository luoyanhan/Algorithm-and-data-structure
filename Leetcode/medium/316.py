from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s):
        cnt = defaultdict(int)
        for each in s:
            cnt[each] += 1
        stack = list()
        for each in s:
            if each not in stack:
                while stack and stack[-1] > each:
                    if cnt[stack[-1]] > 0:
                        stack.pop()
                    else:
                        break
                stack.append(each)
            cnt[each] -= 1
        return ''.join(stack)