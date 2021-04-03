class Solution:
    def validateStackSequences(self, pushed, popped):
        li = list()
        for num in pushed:
            li.append(num)
            while li and popped and li[-1] == popped[0]:
                li.pop()
                popped.pop(0)
        return False if popped else True