import sys


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        # 要获得栈中的最小值，那么就递减
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        if self.stack2 and x > self.stack2[-1]:
            return
        # while self.stack2 and self.stack2[-1]>x:
        #     self.stack2.pop()
        self.stack2.append(x)

    def pop(self) -> None:
        val = self.stack1.pop()
        if self.stack2[-1] == val:
            self.stack2.pop()
        return val

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]


if __name__ == '__main__':
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.push(2)
    s.push(-100)
    print(s.getMin())
    print(s.pop())
    print(s.top())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
