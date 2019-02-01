class Solution:
    def validPalindrome(self, s):
        """
        给定一个非空字符串 s，最多删除一个字符。
        判断是否能成为回文字符串。
        :type s: str
        :rtype: bool
        """
        def isPalindrome(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i=i+1;j=j-1
            return True
        i=0;j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return isPalindrome(i+1,j) or isPalindrome(i,j-1)
            i+=1
            j-=1
        return True

    def validPalindrome1(self,s):
        """
        leetcode最快实例
        :param s:
        :return:
        """
        a=s[::-1]
        if s==a:
            return True
        for i in range(len(s)):
            if a[i]!=s[i]:
                m=s[:i]+s[i+1:]
                n=a[:i]+a[i+1:]
                return m==m[::-1] or n==n[::-1]
        return True



