from heapq import heappop, heappush
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        heap = []
        heappush(heap, 1)
        visited = {1, }
        cnt = 0
        while True:
            cur_ugly = heappop(heap)
            cnt += 1
            if cnt == n:
                return cur_ugly
            for i in primes:
                new_ugly = cur_ugly * i
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heappush(heap, new_ugly)