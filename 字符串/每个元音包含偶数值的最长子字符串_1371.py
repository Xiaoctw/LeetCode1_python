
class Solution:
    '''
    十分巧妙的思想，利用，每个元音字母的奇偶性用一个数字表示
    五位分别代表aeiou
    比如ae就可以用
    11000来表示
    当然也可以通过哈希表来完成
    '''
    def findTheLongestSubstring(self, s: str) -> int:
        pos=[-1]*32
        ans,status=0,0
        pos[0]=status
        for i,c in enumerate(s):
            if c=='a':
                status^=(1<<4)
            elif c=='e':
                status^=(1<<3)
            elif c=='i':
                status^=(1<<2)
            elif c=='o':
                status^=(1<<1)
            elif c=='u':
                status^=(1<<0)
            if pos[status]>=0:
                ans=max(ans,i+1-pos[status])
            else:
                pos[status]=i+1
        return ans

if __name__ == '__main__':
    sol=Solution()
    s='bcbcbc'
    print(sol.findTheLongestSubstring(s))
        