class Solution:
    def minSwapsCouples(self, row):
        """
        两个两个配对,配完对就排除掉,可以用异或方法找到另外一个人
        :type row: List[int]
        :rtype: int
        """
        count=0;l=len(row)
        for i in range(0,l-1,2):
            if row[i]^1==row[i+1]:
                continue
            for j in range(i+2,l):
                if row[i]^1==row[j]:
                    row[j],row[i+1]=row[i+1],row[j]
                    count+=1
                    break
        return count


