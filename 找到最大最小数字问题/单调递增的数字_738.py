class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N==0:
            return 0
        list1=[]
        while N:
            list1.append(N%10)
            N//=10
        list1=list1[::-1]
        min_val=list1[-1]
        list2=[]
        for i in range(len(list1)-1,-1,-1):
            min_val=min(min_val,list1[i])
            list2.append(min_val)
        list2=list2[::-1]
        res=0
        for val in list2:
            res=res*10+val
        return res

if __name__ == '__main__':
    N=10


