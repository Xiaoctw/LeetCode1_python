from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        i,j=0,0
        word_list=[]
        while j<len(s):
            while i<len(s) and s[i]==' ':
                i+=1
            j=i
            if i==len(s):
                break
            while j<len(s) and s[j]!=' ':
                j+=1
            word_list.append(s[i:j])
            i=j
        return ' '.join(word_list[::-1])

if __name__ == '__main__':
    sol=Solution()
    s="a good   example "
    print(sol.reverseWords(s))