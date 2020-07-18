class Solution:
    def generateParenthesis(self, n: int):
        res = list()
        def traceback(S, left, right):
            if len(S) == 2*n:
                res.append(''.join(S))
                return
            if left < n:
                S.append('(')
                traceback(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                traceback(S, left, right+1)
                S.pop()
        traceback([], 0, 0)
        return res