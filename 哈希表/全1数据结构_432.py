import collections
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.str_cnt=collections.defaultdict(lambda :0)#添加删除字符串时用这个来判断有无，避免混乱
        self.cnt_strs=collections.OrderedDict()


    def inc(self, key):
        """
        插入一个值为1的key值
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        self.str_cnt[key]+=1
        num=self.str_cnt[key]
        if not self.cnt_strs.__contains__(num):
            self.cnt_strs[num]=[]
        self.cnt_strs[num].append(key)
        if num>1:
            self.cnt_strs[num-1].remove(key)





    def dec(self, key):
        """
        如果key对应的值为1，那么删除掉，或者减一,如果不存在，那么什么也不做
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if not self.str_cnt.__contains__(key):
            return
        num=self.str_cnt[key]
        self.str_cnt[key]-=1
        self.cnt_strs[num].remove(key)
        if num>1:
            self.cnt_strs[num-1].append(key)


    def getMaxKey(self):
        """
        返回key中值最大的任何一个
        Returns one of the keys with maximal value.
        :rtype: str
        """
        lis=[]
        for l in list(self.cnt_strs.values()):
            lis.extend(l)
        return "" if len(lis)==0 else lis[-1]

    def getMinKey(self):
        """
        返回key中值最小的任何一个
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        lis = []
        for l in list(self.cnt_strs.values()):
            lis.extend(l)
        return "" if len(lis) == 0 else lis[0]

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
obj=AllOne()
obj.inc("1")
obj.inc("1")
obj.inc("2")
obj.inc("2")
obj.dec("2")
obj.dec("2")
obj.dec("1")
obj.dec("1")
print(obj.getMinKey())
print(obj.getMinKey())