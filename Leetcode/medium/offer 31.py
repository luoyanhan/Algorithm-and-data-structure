from collections import deque
class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = deque()
        idx = 0
        for num in pushed:
            stack.append(num)
            #不用检查idx会不会超出最大长度，因为上面有for,只有能pop才可以+1
            while stack and popped[idx] == stack[-1]:
                stack.pop()
                idx += 1
        return not stack


class Solution:
    def validateStackSequences(self, pushed, popped):
        idx_push = 0
        idx_pop = 0
        for num in pushed:
            pushed[idx_push] = num
            while idx_push >= 0 and pushed[idx_push]==popped[idx_pop]:
                idx_push -= 1
                idx_pop += 1
            idx_push += 1
        return idx_push == 0