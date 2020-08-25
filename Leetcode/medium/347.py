class Solution:
    def topKFrequent(self, nums, k):
        from collections import defaultdict
        visited = defaultdict(int)
        for num in nums:
            visited[num] += 1
        tmp = list(visited.items())
        tmp.sort(key=lambda x: x[1], reverse=True)
        res = [tmp[i][0] for i in range(k)]
        return res