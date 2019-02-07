class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ans=[]
        while A or B:
            if len(ans)>=2 and ans[-1]==ans[-2]:
                writeA=ans[-1]=='b'
            else:
                writeA=A>=B
            if writeA:
                ans.append('a')
                A-=1
            else:
                B-=1
                ans.append('b')
        return "".join(ans)

