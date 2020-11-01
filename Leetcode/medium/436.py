class Solution:
    def findRightInterval(self, intervals):
        pre_li = [(intervals[i][0], i) for i in range(len(intervals))]
        pre_li.sort()
        res = list()
        def binary_range(target, pre_li):
            left = 0
            right = len(pre_li) - 1
            while left < right:
                mid = (left+right) // 2
                if pre_li[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid
            return pre_li[left][1] if pre_li[left][0] >= target else -1
        for each in intervals:
            idx = binary_range(each[-1], pre_li)
            res.append(idx)
        return res



class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        res = [-1 for i in range(n)]
        start_sort = sorted(intervals, key=lambda x: x[0])
        end_sort = sorted(intervals, key=lambda x: x[1])
        idx = 0
        for end in end_sort:
            while idx < n:
                if start_sort[idx][0] >= end[1]:
                    res[intervals.index(end)] = intervals.index(start_sort[idx])
                    break
                else:
                    idx += 1
        return res

print(Solution().findRightInterval([[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]))
