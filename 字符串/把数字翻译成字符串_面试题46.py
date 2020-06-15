class Solution:
    def __init__(self):
        self.cnt=0
        self.dic1={i:c for i,c in enumerate('abcdefghijklmnopqrstuvwxyz')}
    def translateNum(self, num: int) -> int:
        num_list=[]
        num_list.append(num % 10)
        num //= 10
        while num:
            num_list.append(num%10)
            num//=10
        self.dfs(num_list[::-1],0,[])
        return self.cnt

    def dfs(self,num_list,idx,list1):
        if idx>=len(num_list):
            self.cnt+=1
            return
        list1.append(self.dic1[num_list[idx]])
        self.dfs(num_list,idx+1,list1)
        list1.pop()
        if idx+1<len(num_list) and num_list[idx]!=0:
            if num_list[idx]*10+num_list[idx+1]<=25:
                c=self.dic1[(num_list[idx]*10+num_list[idx+1])]
                list1.append(c)
                self.dfs(num_list,idx+2,list1)
                list1.pop()

if __name__ == '__main__':
    sol=Solution()
    num=5060312
    print(sol.translateNum(num))

