class Solution:
    def prevPermOpt1(self, A):
        length = len(A)
        i = length - 2
        while i >= 0:
            if A[i] > A[i+1]:
                j = length-1
                max_num = -1
                max_index = -1
                while j >= i+1:
                    if A[j] >= max_num and A[j] < A[i]:
                        max_num = A[j]
                        max_index = j
                    j -= 1
                A[i], A[max_index] = A[max_index], A[i]
                break
            i -= 1
        return A

print(Solution().prevPermOpt1([3,1,1,3]))