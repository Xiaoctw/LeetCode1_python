class Solution:
    def decodeString(self, s: str) -> str:
        i=0
        stack=[]
        num=1
        tem_res=''
        while i<len(s):
            if s[i]=='[':
                stack.append((tem_res,num))
                tem_res=''
                num=1
            elif s[i] in '0123456789':
                tem=0
                while s[i] in '0123456789':
                    tem=tem*10+int(s[i])
                    i+=1
                num=tem
                i-=1
            elif s[i]==']':
                res,pre_num=stack.pop()
                tem_res=res+pre_num*tem_res
            else:
                tem_res=tem_res+s[i]
            i+=1
        return tem_res

if __name__ == '__main__':
    sol=Solution()
    print(sol.decodeString('3[2[4[c]e]4[r2[e]]'))
    print(sol.decodeString('3[a]2[bc]'))
