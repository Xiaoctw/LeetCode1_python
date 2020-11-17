import heapq

nums = [1, 3, 4, 5, 6, 2, 3, 2, 7, 4, 5, 6, 1, 3, 5]

if __name__ == '__main__':
    heapq.heappush(nums, 3)
    heapq.heapify(nums)
    print(nums)
    #只有这两个函数可以传入key
    nlargest=heapq.nlargest(4,nums, key=lambda x: x)
    nsmallest=heapq.nsmallest(4,nums,key=lambda x:x)
    print(nlargest)
    print(nsmallest)
