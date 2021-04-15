class Solution:
    def evalRPN(self, tokens):
        stack = list()
        for each in tokens:
            try:
                num = int(each)
            except:
                right = stack.pop()
                left = stack.pop()
                if each == '+':
                    num = left + right
                elif each == '-':
                    num = left - right
                elif each == '*':
                    num = left * right
                else:
                    num = int(left / right)
            stack.append(num)
        return stack[0]



print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

