class Solution:
    def dailyTemperatures(self, T):
        stack = [0]
        length = len(T)
        res = [0]*length
        for i in range(1, length):
            while stack and T[i] > T[stack[-1]]:
                res[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return res



print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
