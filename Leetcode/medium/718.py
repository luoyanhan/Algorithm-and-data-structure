# 滑动窗口(break是优化)
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def inner(start_a, start_b, length):
            ret = 0
            k = 0
            for i in range(length):
                if A[start_a+i] == B[start_b+i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret

        l_a, l_b = len(A), len(B)
        ret = 0
        for i in range(l_a):
            length = min(l_b, l_a-i)
            if length <= ret:
                break
            ret = max(ret, inner(i, 0, length))
        for i in range(l_b):
            length = min(l_a, l_b-i)
            if length <= ret:
                break
            ret = max(ret, inner(0, i, length))
        return ret



# 动态规划
class Solution:
    def findLength(self, A, B) -> int:
        l_a, l_b = len(A), len(B)
        dp = [[0]*(l_a+1) for _ in range(l_b+1)]
        ans = 0
        for i in range(l_a-1, -1, -1):
            for j in range(l_b-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    ans = max(ans, dp[i][j])
        return ans


# 哈希+二分查找
class Solution:
    def findLength(self, A, B) -> int:
        pass