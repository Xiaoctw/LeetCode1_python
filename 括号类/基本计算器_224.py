class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        tem_res=0
        flag=True
        i=0
        _len=len(s)
        while i<_len:
            c=s[i]
            if c=='(':
                stack.append((tem_res,flag))
                tem_res=0
                flag=True
            if c==')':
                res,flag=stack.pop()
                if flag:
                    tem_res+=res
                else:
                    tem_res=res-tem_res
            if c in '123456789':
                val=int(c)
                while i+1<_len and s[i+1] in '123456789':
                    val=val*10+int(s[i+1])
                    i+=1
                if flag:
                    tem_res+=val
                else:
                    tem_res-=val
            if c=='+':
                flag=True
            if c=='-':
                flag=False
            i+=1
        return tem_res
