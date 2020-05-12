import sys
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        栈中元素和最小值为一一对应的
        """
        self.stack=[]
        self.minstack=[sys.maxsize]



    def push(self, x: int) -> None:
        self.stack.append(x)
        self.minstack.append(min(x,self.minstack[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()