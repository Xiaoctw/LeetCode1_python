from typing import *
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j=len(num1)-1,len(num2)-1
        tem=0
        list1=[]
        dic1={'1':1,'0':0,'2':2,'3':3,'4':4,'5':5,'6':6,
              '7':7,'8':8,'9':9}
        while i>=0 and j>=0:
            # print(num1[i])
            # print(num2[j])
            list1.append(str((tem+dic1[num1[i]]+dic1[num2[j]])%10))
            tem=(tem+dic1[num1[i]]+dic1[num2[j]])//10
            i-=1
            j-=1
        while i>=0:
            list1.append(str((tem + dic1[num1[i]] ) % 10))
            tem = (tem + dic1[num1[i]]) // 10
            i-=1
        while j>=0:
            list1.append(str((tem + dic1[num2[j]]) % 10))
            tem = (tem  + dic1[num2[j]]) // 10
            j-=1
        if tem>0:
            list1.append('1')
        return ''.join(list1[::-1])

if __name__ == '__main__':
    sol=Solution()
    num1='666'
    num2='444'
    print(sol.addStrings(num1,num2))