class Solution:
    def merge(self, intervals):
        if not intervals:
            return list()
        intervals.sort(key=lambda x: x[0])
        result = list()
        first = intervals.pop(0)
        result.append(first)
        while intervals:
            cur = intervals.pop(0)
            target = result.pop()
            if cur[0] <= target[1]:
                new = [target[0], max(cur[1], target[1])]
                result.append(new)
            else:
                result.append(target)
                result.append(cur)
        return result
