class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = list()
        for each in S:
            if each == '(':
                stack.append(each)
            else:
                top = stack.pop()
                if top == '(':
                    result = 1
                else:
                    second = stack.pop()
                    if second == '(':
                        result = 2*top
                    else:
                        result = second+top
                if len(stack) > 1:
                    first = stack.pop()
                    if first != '(':
                        stack.append(first + result)
                    else:
                        stack.append(first)
                        stack.append(result)
                else:
                    stack.append(result)
        return sum(stack)




print(Solution().scoreOfParentheses("()()"))