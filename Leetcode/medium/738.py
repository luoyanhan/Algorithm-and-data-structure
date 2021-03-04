class Solution:
    def monotoneIncreasingDigits(self, N):
        li = [int(each) for each in str(N)]
        length = len(li)
        if length <= 1:
            return N
        idx = 1
        while idx < length and li[idx-1] <= li[idx]:
            idx += 1
        if idx < length:
            while idx > 0 and li[idx-1] > li[idx]:
                li[idx-1] -= 1
                idx -= 1
        for i in range(idx+1, length):
            li[i] = 9
        return ''.join([str(each) for each in li])



print(Solution().monotoneIncreasingDigits(332))
