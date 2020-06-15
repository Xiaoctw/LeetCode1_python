class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1={}
        miss_number=0 #记录缺失字母的个数
        for c in t:
            if c not in dic1:
                dic1[c]=1
                miss_number+=1
            else:
                dic1[c]+=1
        l, r = 0, 0
        min_len=len(s)
        min_l=-1
        while r<len(s):
            if s[r] in dic1:
                dic1[s[r]]-=1
                #有可能减到负数，但是负数也无所谓
                if dic1[s[r]]==0:
                    miss_number-=1
            while miss_number==0:
                if r-l+1<=min_len:
                    min_len=r-l+1
                    min_l=l
                if s[l] in dic1:
                    dic1[s[l]]+=1
                    if dic1[s[l]]>0:#又缺失了
                        miss_number+=1
                l+=1
            r+=1
        if min_l==-1:
            return ''
        return s[min_l:min_l+min_len]

if __name__ == '__main__':
    sol=Solution()
    s='A'
    T='A'
    print(sol.minWindow(s,T))
