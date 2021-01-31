from heapq import heappop, heappush
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heappush(heap, 1)
        visited = {1, }
        cnt = 0
        while True:
            cur_ugly = heappop(heap)
            cnt += 1
            if cnt == n:
                return cur_ugly
            for i in [2, 3, 5]:
                new_ugly = cur_ugly*i
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heappush(heap, new_ugly)

