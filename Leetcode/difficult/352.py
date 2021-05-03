class SummaryRanges:

    def __init__(self):
        self.s = set()


    def addNum(self, val):
        self.s.add(val)


    def getIntervals(self):
        li = list(self.s)
        li.sort()
        length = len(li)
        left, right = 0, 0
        res = list()
        for idx in range(1, length):
            if li[idx] == li[right] + 1:
                right = idx
            else:
                res.append([li[left], li[right]])
                left = idx
                right = left
        res.append([li[left], li[right]])
        return res
