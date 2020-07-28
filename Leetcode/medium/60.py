class Solution:
    def getPermutation(self, n: int, k: int):
        factorials = [1]
        nums = ['1']
        for i in range(1, n):
            factorials.append(factorials[-1]*i)
            nums.append(str(i+1))
        k -= 1
        output = list()
        for i in range(n-1, -1, -1):
            idx = k // factorials[i]
            k -= idx*factorials[i]
            output.append(nums[idx])
            del nums[idx]
        return ''.join(output)



print(Solution().getPermutation(3, 3))
