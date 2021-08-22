

max_size=107

class heap:
    #实现最小堆
    def __init__(self):
        self.array=[0]*107
        self.heap_size=0


    def modify(self,idx):
        if self.heap_size==0:
            return
        left=2*idx+1
        right=2*idx+2
        min_idx=idx
        if left<self.heap_size and self.array[min_idx]>self.array[left]:
            min_idx=left
        if right<self.heap_size and self.array[min_idx]>self.array[right]:
            min_idx=right
        if min_idx!=idx:
            self.array[min_idx],self.array[idx]=self.array[idx],self.array[min_idx]
            self.modify(min_idx)

    def add(self,value):
        assert self.heap_size<max_size
        self.array[self.heap_size]=value
        self.heap_size+=1
        par_idx=(self.heap_size-1)//2
        tem_idx=self.heap_size
        while par_idx>=0:
            if self.array[par_idx]<self.array[tem_idx]:
                self.array[par_idx],self.array[tem_idx]=self.array[tem_idx],self.array[par_idx]
            else:
                break
            tem_idx=par_idx
            par_idx=(tem_idx-1)//2


    def pop(self):
        self.array[0],self.array[self.heap_size-1]=self.array[self.heap_size-1],self.array[0]
        print(self.array[self.heap_size-1])
        self.heap_size-=1
        self.modify(0)


    def sort(self):
        #这里假设初始heap里是无序的
        for idx in range(self.heap_size//2+1):
            self.modify(idx)
        print(self.array)
        num=self.heap_size
        for _ in range(num):

            self.pop()

if __name__ == '__main__':
    h=heap()
    # h.add(1)
    # h.add(4)
    # h.add(3)
    # h.add(5)
    # h.add(2)
    # print(h.array[:h.heap_size])
    # h.pop()
    # print(h.array[:h.heap_size])
    h.array=[1,3,4,2,6,4,3,6]
    h.heap_size=8
    h.sort()
    print(h.array)







