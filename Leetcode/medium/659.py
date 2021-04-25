import heapq
from collections import defaultdict


class Solution:
    def isPossible(self, nums):
        mapper = defaultdict(list)
        for num in nums:
            if num - 1 not in mapper or len(mapper[num - 1]) == 0:
                heapq.heappush(mapper[num], 1)
            else:
                min_len = heapq.heappop(mapper[num - 1])
                min_len += 1
                heapq.heappush(mapper[num], min_len)
        for key in mapper:
            if mapper[key]:
                if heapq.heappop(mapper[key]) < 3:
                    return False
        return True


from collections import defaultdict


class Solution:
    def isPossible(self, nums):
        remain = defaultdict(int)
        ended = defaultdict(int)
        for num in nums:
            remain[num] += 1
        for num in nums:
            if remain[num] > 0:
                if ended[num - 1] > 0:
                    ended[num - 1] -= 1
                    ended[num] += 1
                    remain[num] -= 1
                elif remain[num + 1] > 0 and remain[num + 2] > 0:
                    remain[num] -= 1
                    remain[num + 1] -= 1
                    remain[num + 2] -= 1
                    ended[num + 2] += 1
                else:
                    return False
        return True
