# class Solution:
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         left_li = [1] * n
#         right_li = [1] * n
#         for i in range(1, n):
#             left_li[i] = nums[i-1] * left_li[i-1]
#         for i in range(n-2, -1, -1):
#             right_li[i] = right_li[i+1] * nums[i+1]
#         return [left_li[i] * right_li[i] for i in range(n)]


class Solution:  #输出数组不算空间复杂度， 更省空间， res使用append扩展比一开始就[1]*n省空间
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]
        for i in range(1, n):
            res.append(res[-1] * nums[i-1])  #-1比n-1更省空间
        R = nums[-1]
        for i in range(n-2, -1, -1):
            res[i] *= R
            R *= nums[i]
        return res


print(Solution().productExceptSelf([1,2,3,4]))