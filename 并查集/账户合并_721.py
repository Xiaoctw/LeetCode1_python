class Solution:
    def find(self,i):
        if self.findSet[i]!=i:
            n=self.find(self.findSet[i])
            self.findSet[i]=n
        return self.findSet[i]
    def union(self,i,j):
        if i!=j:
            n=self.find(i)
            if n!=self.find(j):
                self.findSet[n]=self.findSet[j]
    def accountsMerge(self, accounts):
        """
        从开始到结束每一个account都对应一个编号,每一个人名也都对应一个编号
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        mailDic={}
        for ct,i in enumerate(accounts):
            for j in i[1:]:
                mailDic[j]=(ct,i[0])#获得所有的邮件,每个邮件对应键值,序号和姓名对应值
        mails={mail:idx for idx,mail in enumerate(mailDic.keys())}#每一个邮件和一个序号唯一对应
        mailNum=len(mails)
        self.findSet=[i for i in range(mailNum)]
        for li in accounts:
            n=len(li)
            for i in range(1,n-1):
                for j in range(i+1,n):
                    self.union(mails[li[i]],mails[li[j]])#同一个人的邮箱进行合并
        dic={}
        mails={j:i for i,j in mails.items()}#序号在前,名称在后
        for i in range(mailNum):
            mail=mails[i]
            n=mailDic[mails[self.find(i)]][0]#n为一个序号,代表account的序号
            if n in dic:
                dic[n].append(mail)
            else:
                dic[n]=[mail]
        nameId={i[0]:i[1] for i in mailDic.values()}
        return [[nameId[i]]+sorted(mail) for i,mail in dic.items()]



