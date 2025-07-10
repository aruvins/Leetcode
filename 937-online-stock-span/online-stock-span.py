class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack
        cur_quote,cur_span = price, 1

        while stack and stack[-1][0] <= cur_quote:
            prev_quote, prev_span = stack.pop()
            cur_span += prev_span

        stack.append((cur_quote,cur_span))

        return cur_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)