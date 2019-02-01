class Solution:
    def isPalindrome(self, s):
        """
        给定一个字符串,判断是否为回文串
        只保留字母和数字,其中字母大小写无所谓
        :type s: str
        :rtype: bool
        """
        lis=[a for a in list(s.upper()) if 'A'<=a<='Z' or '0'<=a<='9']
        length=len(lis)
        for i in range(length//2):
            if lis[i]!=lis[-(i+1)]:
                return False
        return True

if __name__ == '__main__':
    str1="A man, a plan, a canal: Panama"
    str2="0P"
    print(Solution().isPalindrome(str1))
    print(Solution().isPalindrome(str2))
