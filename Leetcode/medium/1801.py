import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders):
        buy, sell = list(), list()
        for price, amount, orderType in orders:
            if orderType == 0:
                while amount > 0 and sell and sell[0][0] <= price:
                    pri, amo = heapq.heappop(sell)
                    amount -= amo
                if amount < 0:
                    heapq.heappush(sell, (pri, -amount))
                elif amount > 0:
                    heapq.heappush(buy, (-price, amount))
            else:
                while amount > 0 and buy and -buy[0][0] >= price:
                    pri, amo = heapq.heappop(buy)
                    amount -= amo
                if amount < 0:
                    heapq.heappush(buy, (pri, -amount))
                elif amount > 0:
                    heapq.heappush(sell, (price, amount))
        return sum([each[1] for each in buy+sell]) % (10**9+7)