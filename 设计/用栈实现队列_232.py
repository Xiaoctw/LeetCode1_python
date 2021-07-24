from typing import *


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            val = self.stack2.pop()
            return val
        else:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)
            return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            val = self.stack2[-1]
            return val
        else:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)
            return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
if __name__ == '__main__':
    que = MyQueue()
    que.push(1)
    que.push(2)
    que.push(3)
    print(que.peek())
    print(que.pop())
    que.push(5)
    que.push(6)
    print(que.pop())
    print(que.pop())
    print(que.pop())
