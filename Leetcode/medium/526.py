class Solution:
    def countArrangement(self, n):
        visited = [False for _ in range(n+1)]
        count = 0
        def inner(pos):
            nonlocal count
            if pos > n:
                count += 1
            for i in range(1, n+1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = True
                    inner(pos+1)
                    visited[i] = False
        inner(1)
        return count