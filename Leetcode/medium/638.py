class Solution:
    def shoppingOffers(self, price, special, needs):
        length = len(price)
        def dfs(needs):
            res = sum(price[i] * needs[i] for i in range(length))
            for each in special:
                remain = needs[:]
                do = True
                for idx in range(length):
                    if remain[idx] < each[idx]:
                        do = False
                        break
                    remain[idx] = remain[idx] - each[idx]
                if do:
                    res = min(res, each[-1] + dfs(remain))
            return res
        return dfs(needs)


class Solution:
    def shoppingOffers(self, price, special, needs):
        length = len(price)
        mapper = dict()
        def dfs(needs):
            if str(needs) in mapper:
                return mapper[str(needs)]
            res = sum(price[i] * needs[i] for i in range(length))
            for each in special:
                remain = needs[:]
                do = True
                for idx in range(length):
                    if remain[idx] < each[idx]:
                        do = False
                        break
                    remain[idx] = remain[idx] - each[idx]
                if do:
                    res = min(res, each[-1] + dfs(remain))
            mapper[str(needs)] = res
            return res
        return dfs(needs)


class Solution:
    def shoppingOffers(self, price, special, needs):
        length = len(price)
        mapper = dict()
        def dfs(needs):
            if str(needs) in mapper:
                return mapper[str(needs)]
            res = sum(price[i] * needs[i] for i in range(length))
            for each in special:
                remain = list()
                do = True
                for idx in range(length):
                    if needs[idx] < each[idx]:
                        do = False
                        break
                    remain.append(needs[idx] - each[idx])
                if do:
                    res = min(res, each[-1] + dfs(remain))
            mapper[str(needs)] = res
            return res
        return dfs(needs)


