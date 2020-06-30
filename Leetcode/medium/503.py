class Solution:
    def nextGreaterElements(self, nums):
        length = len(nums)
        res = [-1] * length
        stack = [0]
        for i in range(1, length):
            while stack and nums[stack[-1]] < nums[i]:
                temp = stack.pop()
                res[temp] = nums[i]
            stack.append(i)
        for i in range(length):
            while stack and nums[stack[-1]] < nums[i]:
                temp = stack.pop()
                res[temp] = nums[i]
        return res


