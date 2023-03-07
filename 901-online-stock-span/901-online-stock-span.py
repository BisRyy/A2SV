class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        left = 1
        while self.stack and left <= len(self.stack) and self.stack[-1 * left][0] <= price:
            left += self.stack[-1 * left][1]  
        self.stack.append((price,left))
        return  self.stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)