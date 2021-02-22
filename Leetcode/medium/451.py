from collections import defaultdict
class Solution:
    def frequencySort(self, s):
        map = defaultdict(int)
        for word in s:
            map[word] += 1
        li = list(map.items())
        li.sort(key=lambda x: x[1], reverse=True)
        res = str()
        for each in li:
            res += each[0]*each[1]
        return res



from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def frequencySort(self, s):
        heap = list()
        map = defaultdict(int)
        for word in s:
            map[word] += 1
        for word in s:
            heappush(heap, (-map[word], word))
        res = str()
        while heap:
            res += heappop(heap)[1]
        return res


from collections import Counter
class Solution:
    def frequencySort(self, s):
        return ''.join([i*j for i, j in Counter(s).most_common()])


from collections import defaultdict
class Solution:
    def frequencySort(self, s):
        map = defaultdict(int)
        for word in s:
            map[word] += 1
        bucket = [list() for _ in range(len(s)+1)]
        for word in map:
            bucket[map[word]].extend(word*map[word])
        res = list()
        for num in range(len(s), 0, -1):
            if bucket[num]:
                res.extend(bucket[num])
        return ''.join(res)
