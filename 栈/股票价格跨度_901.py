class StockSpanner:

    def __init__(self):
        self.stack = []
        self.cnt = 0

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][1] <= price:
            res = max(res, self.cnt - self.stack[-1][0] + 1)
            self.stack.pop()
        if self.stack:
            res = max(res, self.cnt - self.stack[-1][0])
        else:
            res =max(res, self.cnt + 1)
        self.stack.append((self.cnt, price))
        self.cnt += 1
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
if __name__ == '__main__':
    S = StockSpanner()
    print(S.next(1))
    print(S.next(2))
    print(S.next(3))
    print(S.next(4))
    print(S.next(5))
    print(S.next(75))
    print(S.next(85))
