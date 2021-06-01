from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        mapper = defaultdict(list)
        for ticket in tickets:
            mapper[ticket[0]].append(ticket[1])
        for start in mapper:
            mapper[start].sort()
        res = list()
        def dfs(start):
            nonlocal res
            while mapper[start]:
                nxt = mapper[start].pop(0)
                dfs(nxt)
            res.append(start)

        dfs('JFK')
        return res[::-1]


