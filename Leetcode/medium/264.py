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


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        cnt = 1
        i2 = 0
        i3 = 0
        i5 = 0
        while cnt < n:
            nums.append(min(2*nums[i2], 3*nums[i3], 5*nums[i5]))
            if nums[-1] == 2*nums[i2]:
                i2 += 1
            if nums[-1] == 3*nums[i3]:
                i3 += 1
            if nums[-1] == 5*nums[i5]:
                i5 += 1
            cnt += 1
        return nums[-1]

print(Solution().nthUglyNumber(10))

