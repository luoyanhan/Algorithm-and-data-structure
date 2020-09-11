class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.current = 0


    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.current += 1
        x = 0
        for i in range(len(product)):
            idx_price = self.products.index(product[i])
            x += self.prices[idx_price] * amount[i]
        if self.current % self.n == 0:
            return x - (self.discount * x) / 100
        else:
            return x



class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.price = dict()
        for product, price in zip(products, prices):
            self.price[product] = price
        self.n = n
        self.discount = discount
        self.custom_id = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.custom_id += 1
        payment = 0.0
        for k, v in zip(product, amount):
            payment += self.price[k] * v
        if self.custom_id % self.n == 0:
            payment -= payment * self.discount / 100
        return payment
