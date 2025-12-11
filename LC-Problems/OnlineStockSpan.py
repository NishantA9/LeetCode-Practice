class StockSpanner:
    def __init__(self):
        self.stack = []  # Stack to store pairs of (price, span)
        
    def next(self, price: int) -> int:
        span = 1  # Start with a span of 1 for the current price
        # While stack is not empty and top price is less than or equal to current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]  # Add the span of the popped price
            self.stack.pop()  # Remove the price from stack
        self.stack.append((price, span))  # Push current price and its span
        return span  # Return the span for this price
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)