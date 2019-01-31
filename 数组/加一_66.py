class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length=len(digits)-1
        while length>=0:
            if digits[length]==9:
                digits[length]=0
                length-=1
            else:
                digits[length]+=1
                break
        if digits[0]==0:
            digits=[1]+digits
        return digits
solution=Solution()
print(solution.plusOne([9,9]))
