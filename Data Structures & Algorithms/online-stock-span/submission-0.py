class StockSpanner:

    def __init__(self):
        # Stack stores pairs: (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        # Merge all previous prices that are <= current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        # Store current price with its computed span
        self.stack.append((price, span))

        return span