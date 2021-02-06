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


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        nums = [1]
        cnt = 1
        length = len(primes)
        points = [0 for i in range(length)]
        while cnt < n:
            nums.append(min([primes[i]*nums[points[i]] for i in range(length)]))
            for j in range(length):
                if nums[-1] == primes[j]*nums[points[j]]:
                    points[j] += 1
            cnt += 1
        return nums[-1]