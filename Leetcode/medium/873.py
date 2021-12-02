class Solution:
    def lenLongestFibSubseq(self, arr):
        S = set(arr)
        ans = 0
        length = len(arr)
        for i in range(length-1):
            for j in range(i+1, length):
                cur_l = 2
                x, y = arr[j], arr[i] + arr[j]
                while y in S:
                    cur_l += 1
                    x, y = y, x+y
                ans = max(cur_l, ans)
        return ans if ans > 2 else 0


from collections import defaultdict
class Solution:
    def lenLongestFibSubseq(self, arr):
        longest = defaultdict(lambda: 2)
        mapper = {v: k for k, v in enumerate(arr)}
        length = len(arr)
        ans = 0
        for i in range(length-1):
            for j in range(i+1, length):
                idx = mapper.get(arr[j]-arr[i], None)
                if idx is not None and idx < i:
                    longest[(i, j)] = longest[(idx, i)] + 1
                    ans = max(longest[(i, j)], ans)
        return ans if ans > 2 else 0

