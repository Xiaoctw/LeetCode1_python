class CQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        val=-1
        if self.stack2:
            val=self.stack2.pop()
        else:
            while self.stack1:
                val1=self.stack1.pop()
                self.stack2.append(val1)
            if self.stack2:
                val=self.stack2.pop()
        return val


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
if __name__ == '__main__':
    que=CQueue()
    que.appendTail(1)
    que.appendTail(2)
    que.appendTail(3)
    for _ in range(3):
        val=que.deleteHead()
        print(val)